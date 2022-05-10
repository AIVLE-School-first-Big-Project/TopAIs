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
        if (document.getElementById("service-box").innerHTML.length < 1) {
            document.getElementById('writenextbtn').disabled = true;
        }
        else {
            document.getElementById('writenextbtn').disabled = false;
        }
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
