// 변수 선언
// var areaArr = {
//     '0': {
//         'name' : '럭키아파트',
//         'city': '부산광역시',
//         'county': '사상구',
//         'district': '가야대로',
//         'number1': '284번길',
//         'number2': '2',
//         'latitude':'35.149571',
//         'longitude' :'129.003490'
//     },
//     '1': {
//         'name' : '초가찜',
//         'city': '부산광역시',
//         'county': '사상구',
//         'district': '주례동',
//         'number1': '507',
//         'number2': '14',
//         'latitude':'35.149661644944004',
//         'longitude' :'129.00400623125148'
//     },
//     '2': {
//         'name' : '안오이시오이시스시',
//         'city': '부산광역시',
//         'county': '사상구',
//         'district': '주례3동',
//         'number1': '507',
//         'number2': '21',
//         'latitude':'35.14951479354232',
//         'longitude' :'129.00416721005902'
//     }
// };

var area_x = areaArr[Object.keys(areaArr)[0]]['latitude'];
var area_y = areaArr[Object.keys(areaArr)[0]]['longitude'];
var selectedArea = {};
let markers = new Array();
let infowindows = new Array();

// 구현 내용
var coolroof = new naver.maps.LatLng(area_x, area_y),
    map = new naver.maps.Map('map', {
        center: coolroof,
        zoom: 19
    })
for(key in areaArr) {
    // 마커 생성
    var marker = new naver.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: new naver.maps.LatLng(areaArr[key]['latitude'], areaArr[key]['longitude']), // 마커를 표시할 위치
    });
    var infowindow = new naver.maps.InfoWindow({
        content: [
            '<div class="iw_inner section-padding-10">',
            '   <div id = "name" class = "service-box-title ml-0">' + areaArr[key]['name'] + '</div>',
            '   <div id = "addr" class = "service-box-address ml-0">' + 
            areaArr[key]['city'] + ' ' + 
            areaArr[key]['county'] + ' ' + areaArr[key]['district'] +
            areaArr[key]['number1'] + ' ' + areaArr[key]['number2'] +
            '</div>',
            '   <button id="select-btn" type="submit" onclick = "select(' + key + ')" class="btn select-btn mt-15">SELECT</button>',
            '</div>'
    ].join('')
    })   
    function select(key) {
        if (document.getElementById('select-btn').innerHTML == 'SELECT'){
            var name = document.querySelector('#name').textContent;
            document.getElementById("service-box").innerHTML += ['<div id="innerservice-box" class="service-box mb-15">' +
                '<div class = "service-box-title mt-10">' + document.querySelector('#name').textContent + '</div>' +
                '<div id="'+name+'" class = "service-box-address">' + document.querySelector('#addr').textContent + '</div>' + '</div>']
            document.getElementById('select-btn').style.backgroundColor = 'red';
            document.getElementById('select-btn').style.color = 'white';
            document.getElementById('select-btn').style.border = '1px solid red';
            document.getElementById('select-btn').innerHTML = 'CANCEL';
            selectedArea[key] = areaArr[key];
        }
        else {
            var name = document.querySelector('#name').textContent;
            document.getElementById(name).parentElement.remove();
            document.getElementById('select-btn').style.backgroundColor = 'white';
            document.getElementById('select-btn').style.color = 'lightseagreen';
            document.getElementById('select-btn').style.border = '1px solid lightseagreen';
            document.getElementById('select-btn').innerHTML = 'SELECT';
            delete selectedArea[key];
        }
        document.getElementById('selected_area').value = JSON.stringify(selectedArea);
    }
    markers.push(marker);
    infowindows.push(infowindow);
    
};



map.setMapTypeId(naver.maps.MapTypeId.HYBRID);

function getClickHandler(seq) {
    return function(e) {
        var marker = markers[seq],
            infowindow = infowindows[seq];

        if (infowindow.getMap()) {
            infowindow.close();
        } else {
            infowindow.open(map, marker);
        }
    }
}

console.log(markers)

for (var i=0; ii=markers.length; i<ii, i++) {
    naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
}



// 재완 작성
// var area_x = 35.149571;
// var area_y = 129.003490;
// var building_name = '럭키종합상가';
// var address = '부산광역시 사상구 가야대로284번길 2';
    
// var coolroof = new naver.maps.LatLng(area_x, area_y),
//     map = new naver.maps.Map('map', {
//         center: coolroof,
//         zoom: 19
//     })
    
// var marker = new naver.maps.Marker({
//     map: map,
//     position: coolroof
// });


// var contentString = [
//         '<div class="iw_inner section-padding-10">',
//         '   <div class = "service-box-title ml-0">' + building_name + '</div>',
//         '   <div class = "service-box-address ml-0">' + address + '</div>',
//         '   <button type="submit" id="select-btn" class="btn select-btn mt-15">SELECT</button>',
// 	    '</div>'
// ].join('');

// var infowindow = new naver.maps.InfoWindow({
//     content: contentString
// });

// naver.maps.Event.addListener(marker, "click", function(e) {
//     if (infowindow.getMap()) {
//         infowindow.close();
//     } else {
//         infowindow.open(map, marker);
//     }
// });
// infowindow.close(map, marker);
// window.onload = function(){
//     var t = document.getElementById('select-btn');
//     t.style.color = "red";
// }

// 두번째
// var area_x = 35.149571;
// var area_y = 129.003490;
// var addr_dict = {'name':'럭키', 
//                 'add' : '부산광역시 사상구 가야대로284번길 2', 
//                 'x' : '35.149571', 
//                 'y' :'129.003490'};

// let markers = new Array();
// let infowindows = new Array();

// var coolroof = new naver.maps.LatLng(area_x, area_y),
//     map = new naver.maps.Map('map', {
//         center: coolroof,
//         zoom: 19
//     })

// var positions = [
//     {
//         building_name : addr_dict['name'],
//         address: addr_dict['add'],
//         latlng: new naver.maps.LatLng(addr_dict['x'], addr_dict['y'])
//     },
//     {
//         building_name : '초가찜',
//         address: '부산광역시 사상구 주례동 507-14번지',
//         latlng: new naver.maps.LatLng(35.149661644944004, 129.00400623125148)
//     },
//     {
//         building_name: '오이시스시',
//         address: '부산광역시 사상구 주례3동 507-21',
//         latlng: new naver.maps.LatLng(35.14951479354232, 129.00416721005902)
//     }
// ];


// for (var i = 0; i < positions.length; i ++) {
//     // 마커를 생성합니다
//     var marker = new naver.maps.Marker({
//         map: map, // 마커를 표시할 지도
//         position: positions[i].latlng, // 마커를 표시할 위치
//     })

//     var infowindow = new naver.maps.InfoWindow({
//         content: [
//             '<div class="iw_inner section-padding-10">',
//             '   <div class = "service-box-title ml-0">' + positions[i].building_name + '</div>',
//             '   <div class = "service-box-address ml-0">' + positions[i].address + '</div>',
//             '   <button type="submit" id="select-btn" class="btn select-btn mt-15">SELECT</button>',
//             '</div>'
//     ].join('')
//     })

//     markers.push(marker);
//     infowindows.push(infowindow);

// };
//     map.setMapTypeId(naver.maps.MapTypeId.HYBRID);


// function getClickHandler(seq) {
//     return function(e) {
//         var marker = markers[seq],
//             infowindow = infowindows[seq];

//         if (infowindow.getMap()) {
//             infowindow.close();
//         } else {
//             infowindow.open(map, marker);
//         }
//     }
// }

// for (var i=0; ii=markers.length; i<ii, i++) {
//     console.log(markers[i], getClickHandler(i));
//     naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
// }