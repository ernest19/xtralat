
// var geoloadurl = 'http://127.0.0.1:8000/'

// var map = addtomap('mapid', true);



// var initialbasemap = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
//         attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//     }).addTo(map);

var grayscale = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});


var streets =L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
});





var baseMaps = {
    "Grayscale": grayscale,
    "Streets": streets
};

var overlayMaps = {
    "train": train,
     "region": region,
      "county": county,
};


L.control.layers(baseMaps, overlayMaps).addTo(map);


var options = {
          position: 'topleft',
          lengthUnit: {                 // You can use custom length units. Default unit is kilometers.
            display: 'km',              // This is the display value will be shown on the screen. Example: 'meters'
            decimal: 2,                 // Distance result will be fixed to this value. 
            factor: null,               // This value will be used to convert from kilometers. Example: 1000 (from kilometers to meters)  
            label: 'Distance:'
          }
        };

 

// Load ecowas boundary
// var ecowasboundary = loadVectorlayerfunction(geoserverUrl, "ECOWAS_boundary", 'cite');
// map.addLayer(ecowasboundary)
// $('#ecowasCheck').on('change', function(e){
//   layerTogglefunction(map, ecowasboundary, $(this));
// });


function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7,
        fillColor: 'transparent',
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}






function regionEachFeature(feature, layer) {
    layer.on({
        // mouseover: highlightFeature,
        // mouseout: districtresetHighlight,
        // click: zoomToFeature
    });
}



function countyEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: districtresetHighlight,
        // click: zoomToFeature
    });
}





// Load training data
function regionstyle() {
    return {
        fillColor: 'transparent',
        weight: 3,
        opacity: 1,
        color: 'red',
        dashArray: '3',
        fillOpacity: 1
    }
}

function countystyle() {
    return {
        fillColor: 'transparent',
        weight: 1,
        opacity: 1,
        color: 'black',
        // dashArray: '3',
        fillOpacity: 1
    }
}
var activestore = {
            radius: 5,
            fillColor: 'green', //getColor(feature.properties.year),
            color: '#000',
            weight: 1,
            dashArray: '',
            fillOpacity: 2,
        };

var inactivestore = {
            radius: 5,
            fillColor: 'red', //getColor(feature.properties.year),
            color: '#000',
            weight: 1,
            dashArray: '',
            fillOpacity: 2,
        };



    function otherstyle(feature) {
       var value_f
        value_f = feature.properties.status

        alert(value_f)
         if (value_f == "Inactive (Closed)") {

                return {
                    radius: 5,
                fillColor: 'green', //getColor(feature.properties.year),
                color: '#000',
                weight: 1,
                dashArray: '',
                fillOpacity: 2,
                }
            }
        if (value_f == "Active (Open)") {

            return {
              radius: 5,
            fillColor: 'red', //getColor(feature.properties.year),
            color: '#000',
            weight: 1,
            dashArray: '',
            fillOpacity: 2,
            }
        }
    }


function trainresetHighlight(e) {
    districtboundary.resetStyle(e.target);
}

function trainonEachFeature(feature, layer) {
    layer.bindPopup(`<table class='table table-bordered'><tr><td><b>First Name</b></td><td><b>${feature.properties.owner_first_name} m</b></td></tr><tr><td><b>Last Name</b></td><td><b>${feature.properties.owner_last_name} m</b></td></tr><tr><td><b>Business Name</b></td><td><b>${feature.properties.business_name}</b></td>
            </tr><tr><td><b>Category</b></td><td><b>${feature.properties.category}</b></td></tr><tr><td><b>Status</b></td><td><b>${feature.properties.status}</b></td></tr></table>`);
    layer.on({ 
        click: zoomToFeaturerdis,
        });
};


function zoomToFeaturerdis (e){

map.fitBounds(e.target.getBounds());

  }





// var train = geojsonloadpoint('/trainingjson', train,otherstyle,trainonEachFeature ,"on")
 var train 

 $.ajax({
        url: '/trainingjson',
        async: false,
    }).done(function(res) {

         train = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {

             var value_f
            value_f = feature.properties.status

               if (value_f == "Inactive (Closed)"){
                return L.circleMarker(latlng, inactivestore);
               }
               if (value_f == "Active (Open)"){
                return L.circleMarker(latlng, activestore);
               }
            },

            onEachFeature: trainonEachFeature
        });
        train.bringToFront();
})

map.addLayer(train)



var region =geojsonload("/regionjson",region,regionstyle,regionEachFeature)

var county =geojsonload("/countyjson",region,countystyle,countyEachFeature)
// districtboundary.on('mouseover', function(e){
//     e.layer.bindTooltip(e.layer.feature.properties.district_n).openTooltip();
// })
$('#trainCheck').on('change', function(e) {
    layerTogglefunction(map, train, $(this));
});


 var map =  L.map('mapid', {
        minZoom: 7,
        maxZoom: 20,
        //maxBounds: L.latLngBounds([8.1139, -1.2272], [9.1643, 1.0220]),
        layers: [train, region, county],
        // measureControl: false,
    }).setView([6.31, -10.791], 12);

// L.control.layers(baseMaps, overlayMaps).addTo(map);


// osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//   maxZoom: 19,

//   attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// });
// osm.addTo(map);
// osm.bringToBack();
$('#osmcheck').on('change', function(e){
  layerTogglefunction(map, osm, $(this));
})

