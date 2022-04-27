var area_x = 35.149571;
var area_y = 129.003490;

let markers = new Array();
let infowindows = new Array();

var coolroof = new naver.maps.LatLng(area_x, area_y),
    map = new naver.maps.Map('map', {
        center: coolroof,
        zoom: 19
    })

var positions = [
    {
        building_name : '럭키종합상가',
        address: '부산광역시 사상구 가야대로284번길 2',
        latlng: new naver.maps.LatLng(35.149571, 129.003490)
    },
    {
        building_name : '초가찜',
        address: '부산광역시 사상구 주례동 507-14번지',
        latlng: new naver.maps.LatLng(35.149661644944004, 129.00400623125148)
    },
    {
        building_name: '오이시스시',
        address: '부산광역시 사상구 주례3동 507-21',
        latlng: new naver.maps.LatLng(35.14951479354232, 129.00416721005902)
    }
];


for (var i = 0; i < positions.length; i ++) {
    // 마커를 생성합니다
    var marker = new naver.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
    })

    var infowindow = new naver.maps.InfoWindow({
        content: [
            '<div class="iw_inner section-padding-10">',
            '   <div class = "service-box-title ml-0">' + positions[i].building_name + '</div>',
            '   <div class = "service-box-address ml-0">' + positions[i].address + '</div>',
            '   <button type="submit" id="select-btn" class="btn select-btn mt-15">SELECT</button>',
            '</div>'
    ].join('')
    })

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

for (var i=0; ii=markers.length; i<ii, i++) {
    console.log(markers[i], getClickHandler(i));
    naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
}



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