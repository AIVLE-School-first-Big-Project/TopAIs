from flask import Flask, render_template, request
import numpy as np
import os
import torch
import subprocess
import csv
import pandas as pd
import psycopg2
import requests
import xml.etree.ElementTree as ET
import urllib.request
import datetime


BASE_DIR = os.getcwd()
FILE_LIST = [file for file in os.listdir('./datasets') if file.endswith('.png')]
model = torch.load('./runs/train/result_roof/weights/best.pt')
BASE_DIR = './datasets/'


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        start_x = request.form['start_x']
        start_y = request.form['start_y']
        finish_x = request.form['finish_x']
        finish_y = request.form['finish_y']
        data_folder = get_images((float(start_x), float(start_y)), (float(finish_x), float(finish_y)))
        file_name = subprocess_run(data_folder=data_folder)
        file_name = api_reverse_geocoding(file_name)
        file_name = api_energy(file_name=file_name)
        file_name = api_building(file_name=file_name)
        save_to_postgres(file_name=file_name)
        
    return render_template('home.html')


def get_images(start, finish):
    x = start[0]
    y = start[1]

    x_move = 0.0049877
    y_move = 0.001803899

    x_last = finish[0]
    y_last = finish[1]
    data_folder = str(datetime.datetime.now().date())

    while x <= x_last:
        while y >= y_last:
            urls = ('https://api.vworld.kr/req/image?' +
                'service=image&version=2.0' +
                '&request=getmap' + 
                '&key=483E0418-2F46-3223-80A1-F66D16A24685' +
                '&format=png' + 
                '&errorformat=json' + 
                '&basemap=PHOTO' + 
                '&center=' + str(x) + ',' + str(y) + 
                '&crs=epsg:4326&zoom=18&size=929,437')
            try:
                urllib.request.urlretrieve(urls, './datasets/' + data_folder + '/' + str(x) + ',' + str(y) + '.png')
            except:
                os.mkdir('./datasets/' + data_folder)
                urllib.request.urlretrieve(urls, './datasets/' + data_folder + '/' + str(x) + ',' + str(y) + '.png')
            y = y - y_move
        y = start[1]
        x = x + x_move
    return data_folder

def subprocess_run(data_folder):
    FILE_LIST = [file for file in os.listdir('./datasets/' + data_folder) if file.endswith('.png')]
    subprocess.run(['python', './detect.py', 
                    '--weights', './runs/train/result_roof/weights/best.pt', 
                    '--img', '640',  
                    '--conf', '0.5', 
                    '--name', data_folder,
                    '--source', './datasets/' + data_folder,  
                    '--save-txt'], capture_output=True)
    txt_dir = './runs/detect/' + [folder for folder in os.listdir('./runs/detect/') if folder.startswith(data_folder)][-1] + '/labels/'
    FILE_LIST = [file for file in os.listdir(txt_dir) if file.endswith('.txt')]
    # save coords
    file_name = save_coords(txt_dir=txt_dir, FILE_LIST=FILE_LIST)
    return file_name


def save_coords(txt_dir, FILE_LIST):
    file_name = './coord.csv'
    LATITUDE = -4.141037352666489e-06 
    LONGITUDE = 5.2756524799638424e-06
    
    BASE_COORD = (218.5, 464.5)

    SIZE = 640
    BASE_DIR = txt_dir
    with open(file_name, 'w') as f:
        wr = csv.writer(f)
        wr.writerow(['lat','lon'])
        for file in FILE_LIST:
            with open(BASE_DIR + file, 'r') as txt:
                _coord_y, _coord_x = map(float, file.split('.txt')[0].split(','))
                print('>' * 10)
                print(_coord_x, _coord_y)
                for line in txt.readlines():
                    label, x, y, _, _ = map(float, line.rstrip().split(' '))
                    x, y = SIZE * x, SIZE * y
                    print('*' * 10)
                    print(y, x)
                    new_x = (y * BASE_COORD[0] * 2) / SIZE
                    new_y = (x * BASE_COORD[1] * 2) / SIZE
                    result_x = _coord_x + (new_x - BASE_COORD[0]) * LATITUDE
                    result_y = _coord_y + (new_y - BASE_COORD[1]) * LONGITUDE
                    print(result_x, result_y)
                    wr.writerow([result_x, result_y])
    return file_name

def api_reverse_geocoding(file):
    x_y = pd.read_csv(file)
    df = pd.DataFrame()
    for n in range(0,len(x_y)) :
        add = {}
        file_name = "xy2.csv"
        # x, y값 불러오기
        longitude = x_y['lon'][n]
        latitude = x_y['lat'][n]
        # reverse_geocoding API -> 도로명주소, 지번주소
        url = f'https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?X-NCP-APIGW-API-KEY-ID=efk8ds44x0&X-NCP-APIGW-API-KEY=CX0itE0W1ioC47sUaUviWQw58bL38tXST0vUq8EM&request=coordsToaddr&coords={longitude},{latitude}&sourcecrs=epsg:4326&orders=addr,addr&output=json'
        response = requests.get(url)
        data = response.json()
        print(n, data)
        try:
            # 시군구 행정동 코드
            add['sigungu_code1'] = data['results'][0]['code']['id'][:5]
            add['sigungu_code2'] = data['results'][0]['code']['id'][5:]
            add['type'] = data['results'][0]['land']['type']
            # 건물 이름
            add['building_name'] = data['results'][0]['land']['addition0']['value']
            #  시도명
            add['city'] = data['results'][0]['region']['area1']['name']
            # 구군명
            add['city_1'] = data['results'][0]['region']['area2']['name']
            # 동이름
            add['city_2'] = data['results'][0]['region']['area3']['name']
            # 지번(1)
            add['city_3'] = data['results'][0]['land']['number1']
            # 지번(2)
            add['city_4'] = data['results'][0]['land']['number2']
            # x, y
            add['x'] = x_y['lon'][n]
            add['y'] = x_y['lat'][n]
            df = pd.concat([df, pd.DataFrame([add])])
        except: pass
    # 건물이름 없을시 공백으로 변경
    df['building_name']=df['building_name'].replace('','NoName')
    df['city_4']=df['city_4'].replace('', 0)
    # 산 주소일 경우 제거
    df = df[df['type'] != '2']
    # 중복값 제거
    df = df.drop_duplicates(['sigungu_code1', 'sigungu_code2', 'building_name', 
                            'city', 'city_1', 'city_2', 'city_3', 'city_4'], keep = 'last')
    df.to_csv(file_name, encoding='utf-8-sig')
    return file_name

def api_energy(file_name):
    facility = pd.read_csv(file_name)
    
    # years = ['16', '17', '18', '19', '20', '21']
    years = ['21']
    for year in years:
        facility["electro_"+'20' + year + '08'] = 0
        for n in range(0, len(facility)):#0,len(facility)) :
            url = 'http://apis.data.go.kr/1611000/BldEngyService/getBeElctyUsgInfo'
            bun = ('0000' + str(facility['city_3'][n]))[-4:]
            try: ji = ('0000' + str(int(facility['city_4'][n])))[-4:]
            except: ji = '0000'
            params ={
                'serviceKey' : 'KqeUwY/c3AjiMszOMQ7FG5eXBJMCXQgqwh7Xa5j/mGjdUUUDk6/HNqC+J319L9tBUZuVaKqFiE1BdLrVsT5Shw==', 
                'numOfRows' : '10', 'pageNo' : '1', 
                'sigunguCd' : facility['sigungu_code1'][n], 'bjdongCd' : facility['sigungu_code2'][n], 
                'bun' : bun, 'ji' : ji, 'useYm' : '20' + year + '08' 
            }

            response = requests.get(url, params=params)
            root = ET.fromstring(response.content)
            useQty = None

            try:
                for item in root.findall("body")[0].findall("items")[0].findall("item"):
                    useQty = item.findtext("useQty")
                    useYm = item.findtext("useYm")
                if not useQty is None: 
                    facility["electro_"+'20' + year + '08'][n] = useQty
                    print('20' + year + '08', useQty)
            except: pass
    facility.to_csv('energy.csv', encoding='utf-8-sig')
    return 'energy.csv'

def api_building(file_name):
    facility = pd.read_csv(file_name)
    facility['archArea'] = 0
    facility['etcPurps'] = 'No'
    facility['newPlatPlc'] = 'No'
    for n in range(1,len(facility)) :
        url = 'http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo'
        bun = ('0000' + str(facility['city_3'][n]))[-4:]
        try: ji = ('0000' + str(int(facility['city_4'][n])))[-4:]
        except: ji = '0000'
        archArea = 0
        
        params ={
            'serviceKey' : 'KqeUwY/c3AjiMszOMQ7FG5eXBJMCXQgqwh7Xa5j/mGjdUUUDk6/HNqC+J319L9tBUZuVaKqFiE1BdLrVsT5Shw==', 
            'numOfRows' : '10', 'pageNo' : '1', 
            'sigunguCd' : facility['sigungu_code1'][n], 'bjdongCd' : facility['sigungu_code2'][n], 
            'bun' : bun, 'ji' : ji
        }

        response = requests.get(url, params=params, )
        root = ET.fromstring(response.content)
        print(response.url)
        print(response.content)

        for item in root.findall("body")[0].findall("items")[0].findall("item"):
            archArea = item.findtext("archArea")
            if facility['building_name'][n] == 'NoName':
                if item.findtext("bldNm") is not None:
                    facility['building_name'][n] = item.findtext("bldNm")
                else:
                    facility['building_name'][n] = '-'
            facility['etcPurps'][n] = item.findtext('etcPurps')
            facility['newPlatPlc'][n] = item.findtext('newPlatPlc')
        # 이름 없을시 NoName으로 변경
        facility = facility.replace('NoName','-')
        facility['archArea'][n] = archArea
        if (float(facility['archArea'][n]) != 0.0) and (float(facility['electro_202108'][n]) == 0.0):
            facility['electro_202108'][n] = float(facility['archArea'][n]) * 65
    facility.to_csv('archArea.csv', encoding='utf-8-sig')
    return 'archArea.csv'


def save_to_postgres(file_name):
    facility = pd.read_csv(file_name)
    conn = psycopg2.connect(host='foo', dbname='foo', user='foo-user', password='foo-pwd', port=0000)
    # Cursor 객체 생성 
    cs = conn.cursor()

    query_facility = 'INSERT INTO public."Facility" ' + \
            '(latitude, longitude, area, facility_type) ' + \
            'VALUES '
    query_building = 'INSERT INTO public."Building" ' + \
            '(facility_ptr_id, name, city, county, district, number1, number2, ' + \
            'electro_201608, electro_201708, electro_201808, electro_201908, electro_202008, electro_202108, ' + \
            '"etcPurps", "newPlatPlc") ' + \
            'VALUES '
    cs.execute('SELECT id FROM public."Facility" ORDER BY id DESC LIMIT 1;')

    try:
        idx_ptr = cs.fetchone()[0]
    except:
        idx_ptr = 0

    for i in range(len(facility)):
        fac = facility.iloc[i]
        query_facility += '(' + str(fac['y']) + ',' + str(fac['x']) + ',' + str(fac['archArea']) + ',' + "'''building'''), "
        query_building += "(" + str(idx_ptr+i+1) + ",'" + fac['building_name'] + "','"+ fac['city'] + "','"+ fac['city_1'] + "','"+ fac['city_2'] + "'," + str(fac['city_3']) + ',' + str(fac['city_4']) + ',' + \
            str(fac['electro_201608']) + ',' + str(fac['electro_201708']) + ',' + str(fac['electro_201808']) + ',' + str(fac['electro_201908']) + ',' + str(fac['electro_202008']) + ',' + str(fac['electro_202108']) + ",'" + \
            fac['etcPurps'] + "','"+ fac['newPlatPlc'] + "'), "
    query_facility = query_facility[:-2] + ';'
    query_building = query_building[:-2] + ';'

    print(query_facility)
    print(query_building)
    
    cs.execute(query_facility)
    conn.commit()
    cs.execute(query_building)

    # execute 에 db 에 적용 
    conn.commit()
    conn.close()

    return


if __name__ == "__main__":
    app.run(debug=True)


