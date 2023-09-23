// default map layer
let map = L.map('map', {
    layers: MQ.mapLayer(),
    center: [10.065206, 76.629128],
    zoom: 12
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


navigator.geolocation.watchPosition(success,error);

let marker, circle, zoomed;

function success(pos){
    const lat=pos.coords.latitude;
    const lng=pos.coords.longitude;
    const accuracy=pos.coords.accuracy;

    if(marker){
        map.removeLayer(marker);
        map.removeLayer(circle);
    }


    marker = L.marker([lat,lng]).addTo(map);
    circle = L.circle([lat,lng], { radius: accuracy }).addTo(map);

    if(!zoomed){
        map.fitBounds(circle.getBounds());
    }
    map.setView([lat,lng]);

}

function error(err){
    if(err.code === 1){
        alert("Please allow location access");
    }else{
        alert("Cannot retrieve location");
    }
}

    

    function runDirection(start, end) {
        
        // recreating new map layer after removal
        map = L.map('map', {
            layers: MQ.mapLayer(),
            center: [10.065206, 76.629128],
            zoom: 12
        });
        
        var dir = MQ.routing.directions();

        dir.route({
            locations: [
                start,
                end
            ]
        });
    

        CustomRouteLayer = MQ.Routing.RouteLayer.extend({
            createStartMarker: (location) => {
                var custom_icon;
                var marker;

                custom_icon = L.icon({
                    iconUrl: '../static/assets/red.png',
                    iconSize: [20, 29],
                    iconAnchor: [10, 29],
                    popupAnchor: [0, -29]
                });

                marker = L.marker(location.latLng, {icon: custom_icon}).addTo(map);

                return marker;
            },

            createEndMarker: (location) => {
                var custom_icon;
                var marker;

                custom_icon = L.icon({
                    iconUrl: '../static/assets/blue.png',
                    iconSize: [20, 29],
                    iconAnchor: [10, 29],
                    popupAnchor: [0, -29]
                });

                marker = L.marker(location.latLng, {icon: custom_icon}).addTo(map);

                return marker;
            }
        });
        
        map.addLayer(new CustomRouteLayer({
            directions: dir,
            fitBounds: true
        })); 
    }


// function that runs when form submitted
function submitForm(event) {
    event.preventDefault();

    // delete current map layer
    map.remove();

    // getting form data
    start = document.getElementById("start").value;
    end = document.getElementById("destination").value;

    // run directions function
    runDirection(start, end);

    // reset form
    document.getElementById("form").reset();
}

// asign the form to form variable
const form = document.getElementById('form');

// call the submitForm() function when submitting the form
form.addEventListener('submit', submitForm);
