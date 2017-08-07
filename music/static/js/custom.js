$(function () {

    function initMap() {

        navigator.geolocation.getCurrentPosition(function(position) {
        var location = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

        var mapCanvas = document.getElementById('map');
        var mapOptions = {
            center: location,
            zoom: 16,
            panControl: false,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var map = new google.maps.Map(mapCanvas, mapOptions);
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: markerImage
        });

        var contentString = '<div class="info-window">' +
                '<h3>My Home</h3>' +
                '<div class="info-content">' +
                '</div>' +
                '</div>';

        var infowindow = new google.maps.InfoWindow({
            content: contentString,
            maxWidth: 400
        });

        marker.addListener('click', function () {
            infowindow.open(map, marker);
        });
    });
    }

    google.maps.event.addDomListener(window, 'load', initMap);

});