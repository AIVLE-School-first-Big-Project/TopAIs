var coolroof = new naver.maps.LatLng(35.149561,129.003490),
    map = new naver.maps.Map('map', {
        center: coolroof,
        zoom: 15
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: coolroof
    });
var contentString = [
        '<div class="iw_inner section-padding-10">',
        '   <div class = "service-box-title ml-0">럭키종합상가</div>',
        '   <div class = "service-box-address ml-0">부산 사상구 가야대로284번길 2</div>',
        '   <button type="submit" class="btn select-btn mt-15">SELECT</button>',
	    '</div>'
					
    ].join('');

var infowindow = new naver.maps.InfoWindow({
    content: contentString
});

naver.maps.Event.addListener(marker, "click", function(e) {
    if (infowindow.getMap()) {
        infowindow.close();
    } else {
        infowindow.open(map, marker);
    }
});

infowindow.close(map, marker);