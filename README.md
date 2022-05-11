# TopAIS
![Main](https://user-images.githubusercontent.com/42468323/167663480-471cfd9e-3c5a-483b-a70a-f2830c893f91.png)

## 1. 팀 소개
- 소속: AI 부산경남 1반 1조(13조)
- 조원: 전윤지(조장), 김재완, 신민진, 이원호
## 2.프로젝트 소개
### 프로젝트 기간
- 2022.04.11 ~ 2022.05.11
### 주제
위성 사진을 활용한 도시 환경 개선
<br>
### 주제 선정 배경
- 점점 높아지는 도시의 평균 기온은 냉방 수요를 늘리고, 이는 도시 열섬 현상 등의 원인

- 열대야와 같이 여름철 우리 삶의 질을 하락시키는 현상의 주요 원인

- 이를 해결하기 위해 쿨루프 시공과 같은 대안적인 기술이 진행되고 있으나, 현실적으로 모든 건물을 확인 및 적용하기에는 많은 제약이 존재

- 수 많은 위성에서 매일 엄청난 데이터가 생산

- 방대한 양의 위성 데이터는 산업적으로 활용가치가 높은 빅데이터로 평가

- 인공위성 이미지 데이터를 활용하여 방수 필요 건물을 분류하고 효율적이고 신속한 쿨루프 사업의 적용 방안을 제시

>쿨루프란?
> 시원한 지붕을 의미하는 것으로, 건물 지붕이나 옥상에 태양열을 차단하는 밝은색 계열의 특수 도료를 칠해 지붕에 열기가 축적되는 것을 줄이는 공법

<p align="center">
  <img src="https://cdn.electimes.com/news/photo/202203/301619_501016_1615.jpg"/>
</p>

<br>

## 3. 기대효과
1. 냉방효율 증대로 에너지 효율 개선 및 온실가스 감축효과 기대
2. 도시 자동화 시스템의 범위 확장
3. 지자체 사업 편의성 증대

<p align="center">
  <img src="https://cdn.gjinfocus.com/news/photo/202103/10583_10698_2638.jpg"/>
</p>

> 쿨루프 시공전후의 지붕의 표면 온도측정 사진. (좌) 설치전 (우) 설치후 
> (사진/한국환경산업기술원 보고서)
<br>

## 4. Tech Stack

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/42468323/167661473-aba155e1-a107-4c76-91a0-3903b9cb5a72.png"/>
</p>
<br>

## 5. System Architecture

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/42468323/167651792-aa7dbf5c-ef48-4eb5-9d18-a80fd8a0c821.png"/>
</p>
<br>

## 6. ERD

<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/42468323/167654716-d3f3549c-9bd6-4c75-8d72-8236926b3a34.png"/>
</p>
<br>

## 6. Step to run


```console
$ cd TopAIs
$ python -m venv .venv
$ source .venv/bin/activate
$ python install -r requirements.txt
$ python manage.py runserver
```

