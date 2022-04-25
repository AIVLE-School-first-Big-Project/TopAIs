var area_x = 35.149571;
var area_y = 129.003490;
var building_name = '럭키종합상가';
var address = '부산광역시 사상구 가야대로284번길 2';

var coolroof = new naver.maps.LatLng(area_x, area_y),
    map = new naver.maps.Map('map', {
        center: coolroof,
        zoom: 19
    })

var marker = new naver.maps.Marker({
    map: map,
    position: coolroof
});
    map.setMapTypeId(naver.maps.MapTypeId.HYBRID);
var contentString = [
        '<div class="iw_inner section-padding-10">',
        '   <div class = "service-box-title ml-0">' + building_name + '</div>',
        '   <div class = "service-box-address ml-0">' + address + '</div>',
        '   <button type="submit" id="select-btn" class="btn select-btn mt-15">SELECT</button>',
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
window.onload = function(){
    var t = document.getElementById('select-btn');
    t.style.color = "red";
}