// var map = L.map('mapid').setView([51.505, -0.09], 13);


var littleton = L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.'),
    denver    = L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.'),
    aurora    = L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.'),
    golden    = L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.');


var cities = L.layerGroup([littleton, denver, aurora, golden]);





var map = L.map('mapid', {
    center: [6.31, -10.791],
    zoom: 10,
    // ÷layers: [grayscale, cities]
}).setView([6.31, -10.791], 12);;



 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);



  var  streets   = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}),

 google =L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
        maxZoom: 20,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });

function trainonEachFeature(feature, layer) {
    layer.bindPopup(`<table class='table table-bordered'><tr><td><b>First Name</b></td><td><b>${feature.properties.owner_first_name} m</b></td></tr><tr><td><b>Last Name</b></td><td><b>${feature.properties.owner_last_name} m</b></td></tr><tr><td><b>Business Name</b></td><td><b>${feature.properties.business_name}</b></td>
            </tr><tr><td><b>Category</b></td><td><b>${feature.properties.category}</b></td></tr><tr><td><b>Status</b></td><td><b>${feature.properties.status}</b></td></tr></table>`);
    layer.on({ 
        click: zoomToFeature,
        });
};

function zoomToFeature(e)
{
  var latLngs = [e.target.getLatLng()];
  var markerBounds = L.latLngBounds(latLngs);
  map.fitBounds(markerBounds);
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

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#15f4ee',
        dashArray: '',
        fillOpacity: 0.7,
        fillColor: 'transparent',
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function reghighlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#fc4',
        dashArray: '',
        fillOpacity: 0.7,
        fillColor: 'transparent',
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

 var customOptions = {'maxWidth': '900','className' : 'custom'}

function regionEachFeature(feature, layer) {
     labeltoshow = '<div  id="tblrep" > </div>'
   layer.bindTooltip(` ${feature.properties.name} `);
    layer.on({
        mouseover: reghighlightFeature,
        mouseout: regionresultoneach,
        click: regionzoomToFeature
    });
}


function zoomToFeature(e) {
// map.fitBounds(e.target.getBounds());
  $.get('/distdetails/?dist=' + e.target.feature.id, function(data) {
   $('#distdetails').html(data)
});


}

function regionzoomToFeature(e) {
// map.fitBounds(e.target.getBounds());
  $.get('/distdetails/?dist=' + e.target.feature.id, function(data) {
   $('#distdetails').html(data)
});
}


function countyEachFeature(feature, layer) {
    labeltoshow = '<div  id="distdetails" > </div>'
    // layer.bindPopup(labeltoshow,customOptions);
    layer.bindTooltip(` ${feature.properties.name} `);
    layer.on({
        mouseover: highlightFeature,
        mouseout: districtresultoneach,
        click: zoomToFeature
    });
}


function regionresultoneach(e) {
    region.resetStyle(e.target);
}


function districtresultoneach(e) {
    county.resetStyle(e.target);
}




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
        weight: 2,
        opacity: 1,
        color: 'black',
        // dashArray: '3',
        fillOpacity: 1
    }
}








var region =geojsonload("/regionjson",region,regionstyle,regionEachFeature)

var county =geojsonload("/countyjson",region,countystyle,countyEachFeature)


// var baseMaps = {
//     "Grayscale": grayscale,
//     "Streets": streets
// };





var testData , heatmapLayer
 $.get('/heatmap/', function(data) {
            
     testData = {
      max: 8,
      data: data
    };

    var cfg = {
  // radius should be small ONLY if scaleRadius is true (or small radius is intended)
  // if scaleRadius is false it will be the constant radius used in pixels
  "radius": 2,
  "maxOpacity": .8,
  // scales the radius based on map zoom
  "scaleRadius": true,
  // if set to false the heatmap uses the global maximum for colorization
  // if activated: uses the data maximum within the current map boundaries
  //   (there will always be a red spot with useLocalExtremas true)
  "useLocalExtrema": true,
  // which field name in your data represents the latitude - default "lat"
  latField: 'lat',
  // which field name in your data represents the longitude - default "lng"
  lngField: 'lng',
  // which field name in your data represents the data value - default "value"
  valueField: 'count'
};


heatmapLayer = new HeatmapOverlay(cfg);
heatmapLayer.setData(testData);
    // $('#results_container').html(data);
  });


var baseMaps = {
    "<span style='color: gray'>Satellite</span>": google,
    "Streets": streets
};


var overlayMaps = {
    "POS": train,
    "Region/District":region,
    "Territory":county,
    // "Heatmap":heatmapLayer,
};


L.control.layers(baseMaps, overlayMaps).addTo(map);

 // var sidebar = L.control.sidebar('sidebar').addTo(map);




