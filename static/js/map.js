var coolroof = new naver.maps.LatLng(35.149561,129.003490),
    map = new naver.maps.Map('map', {
        center: coolroof,
        zoom: 15
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: coolroof
    });