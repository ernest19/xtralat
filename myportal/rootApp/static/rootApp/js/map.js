   var map = L.map('mapid', {
       // maxBounds: L.latLngBounds([3.7388, -4.262], [12.1748, 2.200]),
        center: [6.31, -10.791],
       zoomControl: false,



   }).setView([6.31, -10.791], 8);;

   // setView([9.099, -1.000], 7);


   googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
       maxZoom: 20,
       subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
   }).addTo(map);


   function geojsonload(url, geodata, style, onEachFeature, check) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {

        geodata = L.geoJSON(res, { style: style, onEachFeature: onEachFeature });
        geodata.bringToBack();
        if (check) { map.addLayer(geodata) }
         geodata.bringToBack();

    })

    return geodata
}


   function mapdisbled(map) {
       map.touchZoom.disable();
       map.doubleClickZoom.disable();
       // map.scrollWheelZoom.disable();
       //map.dragging.disable();
       map.keyboard.disable();
       if (map.tap) map.tap.disable();
   }



   L.control.coordinates({ position: "bottomleft" }).addTo(map);




   $('#zoomin').on('click', function() {

       mapdisbled(map);
       map.zoomIn(1);
   })


   $('#zoomout').on('click', function() {

       mapdisbled(map);
       map.zoomOut(1);
   })



   function autoquick1(code, ftype) {
       getextent('/extent/' + code + '/' + ftype + '/', map);
       // selectmap('/highlight/' + code  + '/' + ftype + '/',map,'',selectstyle)
   }



   function getextent(url, map) {
       $.get(url, function(data) { map.fitBounds([
               [data[1], data[0]],
               [data[3], data[2]]
           ]) })
   }

   //Highlightmap style
   function highlightstyle() {
       return {
           fillColor: 'transparent',
           weight: 4,
           opacity: 1,
           color: 'cyan',
           dashArray: '',
           fillOpacity: '1'
       };

   }

   //selecymap style
   function selectstyle() {
       return {
           fillColor: 'transparent',
           weight: 4,
           opacity: 1,
           color: '#f00',
           dashArray: '',
           fillOpacity: '1'
       };

   }




   var selectfeaturezone;

   function selectmap(url, map, typem, mnh) {
       $.get(url, function(data) {
           if (selectfeaturezone != undefined) {
               map.removeLayer(selectfeaturezone)
           }
           if (typem == 'point') {
               selectfeaturezone = new L.GeoJSON(data, { pointToLayer: mnh }).addTo(map).bringToFront();
           } else {
               selectfeaturezone = new L.GeoJSON(data, { style: mnh }).addTo(map).bringToBack();
           }
       }).done(function() {}).fail(function() {});
   }








   //Autocomplete function
   var options = {
       url: function(phrase) {
           return "/autocompleteview/?phrase=" + phrase;
       },
       placeholder: "Search by region,district,plantation",
       template: {
           type: "description",
           fields: {
               description: "type"
           },
       },
       getValue: "name",
       requestDelay: 500,
       list: {
           match: {
               enabled: true
           },
           maxNumberOfElements: 10,
           showAnimation: {
               type: "slide",
               time: 300
           },
           hideAnimation: {
               type: "slide",
               time: 300
           },
           onSelectItemEvent: function() {
               var code = $("#inputsearch").getSelectedItemData().code;
               var ftype = $("#inputsearch").getSelectedItemData().type;
               autoquick1(code, ftype)
           },
           onChooseEvent: function() {
               var code = $("#inputsearch").getSelectedItemData().code;
               var ftype = $("#inputsearch").getSelectedItemData().type;
               autoquick1(code, ftype)

           },
           onKeyEnterEvent: function() {
               var code = $("#inputsearch").getSelectedItemData().code;
               var ftype = $("#inputsearch").getSelectedItemData().type;
               autoquick1(code, ftype)
           },
           onShowListEvent: function() {
               $(".circlemainsmallsearch").addClass("hidden");
           },
           onLoadEvent: function() {
               $(".circlemainsmallsearch").removeClass("hidden");
           }
       },
       theme: "blue-light",
       //theme: "round"
   };
   $("#inputsearch").easyAutocomplete(options);






   $("#layerbtn").click(function() {
       // alert("goop")
       $("#basemap").slideToggle("slow");
   });

   var options = {
       position: 'topleft', // Leaflet control position option
       circleMarker: { // Leaflet circle marker options for points used in this plugin
           color: 'red',
           radius: 2
       },
       lineStyle: { // Leaflet polyline options for lines used in this plugin
           color: 'red',
           dashArray: '1,6'
       },
       lengthUnit: { // You can use custom length units. Default unit is kilometers.
           display: 'km', // This is the display value will be shown on the screen. Example: 'meters'
           decimal: 2, // Distance result will be fixed to this value. 
           factor: null, // This value will be used to convert from kilometers. Example: 1000 (from kilometers to meters)  
           label: 'Distance:'
       },
       angleUnit: {
           display: '&deg;', // This is the display value will be shown on the screen. Example: 'Gradian'
           decimal: 2, // Bearing result will be fixed to this value.
           factor: null, // This option is required to customize angle unit. Specify solid angle value for angle unit. Example: 400 (for gradian).
           label: 'Bearing:'
       }
   }

  L.control.scale().addTo(map);
   // L.control.ruler(options).addTo(map);

   L.control.mousePosition().addTo(map);

//    L.control.browserPrint({
//     title: 'hellooooo',

// }).addTo(map);



L.control.browserPrint({
       
    printModes: ["Portrait", "Landscape", "Auto", "Custom"],
    manualMode: true // use true if it's debug and/or default button is okay for you, otherwise false.
    }).addTo(map);

  document.querySelector("#custom_print_button").addEventListener("click", function(){
    var modeToUse = L.control.browserPrint.mode.auto();
    map.printControl.print(modeToUse);

      // alert( $("#mapotitle").val())

      var titt = $("#mapotitle").val()

      $( ".grid-print-container" ).append("<h2 id='tittop'>" + titt + "</h2>");


  });



// var customActionToPrint = function(context, mode) {
//   return function() {
//     window.alert("We are printing the MAP. Let's do Custom print here!");
//     context._printCustom(mode);
//   }
// }

// L.control.browserPrint({
//   title: 'Just print me!',
//   documentTitle: 'Map printed using leaflet.browser.print plugin',
//    manualMode: true ,
//   closePopupsOnPrint: false,
//   printModes: [
//     L.control.browserPrint.mode.landscape("TABLOID VIEW", "tabloid"),
//     L.control.browserPrint.mode("Alert", "User specified print action", "A6", customActionToPrint, false),
//     L.control.browserPrint.mode.landscape(),
//     "Portrait",
//     L.control.browserPrint.mode.auto("Automatico", "B4"),
//     L.control.browserPrint.mode.custom("Séléctionnez la zone", "B5")
//   ],
//   // manualMode: false
// }).addTo(map);
























   var style = {
       color: 'red',
       opacity: 1.0,
       fillOpacity: 0,
       weight: 2,
       clickable: false
   };
   L.Control.FileLayerLoad.LABEL = '<img class="icon" src="/static/rootApp/leaflet/folder.svg" alt="file icon"/>';
   control = L.Control.fileLayerLoad({
       fitBounds: true,
       layerOptions: {
           style: style,
           pointToLayer: function(data, latlng) {
               return L.circleMarker(
                   latlng, { style: style }
               );
           }
       }
   });
   // control.addTo(map);
   // control.loader.on('data:loaded', function(e) {
   //     var layer = e.layer;
   //     console.log(layer);
   // });



   function getColor(d) {
       return d > 1000 ? '#800026' :
           d > 500 ? '#BD0026' :
           d > 200 ? '#E31A1C' :
           d > 100 ? '#FC4E2A' :
           d > 50 ? '#FD8D3C' :
           d > 20 ? '#FEB24C' :
           d > 10 ? '#FED976' :
           '#FFEDA0';
   }



   L.LegendControl = L.Control.extend({
       onAdd: function(map) {
           var labels = [];
           var div = L.DomUtil.create('div', 'info legend');
           // var grades = [0, 10, 20, 50, 100, 200, 500, 1000];
           // var labels = [];
           // var from;
           // var to;

           // for (var i = 0; i < grades.length; i++) {
           //     from = grades[i];
           //     to = grades[i + 1];
           html = ('<h2 style="text-align: center;"><strong>Legend</strong> </h2>')
           html += ('<ul class="info1" style="background-color:white"> ')
           html += ('<li>Region Boundary<span class="legendbox reg1"> </span></li> ')
           html += ('<li>District Boundary<span class="legendbox district1"> </span></li>')

           html += ('<li>Protected Area<span class="legendbox protect1" style=""> </span></li>')

           html += ('<li> Plantation<span class="legendbox platn1"> </span></li>')
           // html += ('<tr> <th>Year of Establishment</th> <td>N/A</td></tr>')
           // html += ('<tr> <th>Area reported planted</th> <td>N/A</td></tr>')
           // html += ('<tr> <th>Area verified planted</th> <td>N/A</td></tr>')
           // html += ('<tr> <th>Percentage survival</th> <td>70%</td></tr>')
           html += ('</ul>')


           html += ('</table>')
           html += ('</div >')


           labels.push(html);
           // }

           div.innerHTML = labels.join('');
           return div;
       }
   });



   L.legendControl = function(options) {
       return new L.LegendControl(options);
   };

   // Here we are creating control to show it on the map;
   // L.legendControl({ position: 'bottomright' }).addTo(map);




L.control.rose = L.control({position: "bottomleft"});

L.control.rose .onAdd = function(map) {
    var div = L.DomUtil.create("div", "info asd");
    div.innerHTML = '<img id="arrow" leaflet-browser-print-content src="/static/rootApp/img/arrow.png" style="width: 70px;height: 70px;position: absolute;top: 24vh;z-index: 99999;">';
    return div;
}

// L.control.rose .addTo(map);


var optionmeasure = {
  position: 'topleft' ,
  primaryAreaUnit: 'hectares',
}

var measureControl = new L.Control.Measure(optionmeasure);
measureControl.addTo(map);






   map.on("browser-print-start", function(e) {
       /*on print start we already have a print map and we can create new control and add it to the print map to be able to print custom information */
       L.legendControl({ position: 'bottomright' }).addTo(e.printMap);

       // L.legendControl({ position: 'bottomleft' }).addTo(e.printMap);

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
        url: '/mapapp/trainingjson/',
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

// map.addLayer(train)
// train.bringToFront()



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
        // mouseover: reghighlightFeature,
        // mouseout: regionresultoneach,
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
  $.get('/mapapp/distdetails/?dist=' + e.target.feature.id, function(data) {
   $('#distdetails').html(data)
});
}


function countyEachFeature(feature, layer) {
    labeltoshow = '<div  id="distdetails" > </div>'
    // layer.bindPopup(labeltoshow,customOptions);
    layer.bindTooltip(` ${feature.properties.territoryname} `);
    layer.on({
        // mouseover: highlightFeature,
        // mouseout: districtresultoneach,
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








var region =geojsonload("/mapapp/regionjson",region,regionstyle,regionEachFeature , "check")

var county =geojsonload("/mapapp/countyjson",region,countystyle,countyEachFeature)





    $('#regcheck').on('change', function() {
        var man = $('#regcheck').is(':checked');
        // if (dismap == undefined){
        //   districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)
        // }
        if (man == true) {
            if (region) {
                map.addLayer(region);
                region.bringToBack()
            }

        } else {
            map.removeLayer(region);
            // map.removeLayer(districtcapital);
        }
    })



    $('#districtcheck').on('change', function() {
        var man = $('#districtcheck').is(':checked');
        // if (dismap == undefined){
        //   districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)
        // }
        if (man == true) {
            if (county) {
                map.addLayer(county);
            }

        } else {
            map.removeLayer(county);
            // map.removeLayer(districtcapital);
        }
    })


    $('#protectcheck').on('change', function() {
        var man = $('#protectcheck').is(':checked');
        // if (dismap == undefined){
        //   districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)
        // }

        if (man == true) {
            if (train) {
                map.addLayer(train);
                train.bringToFront()
            }

        } else {
            map.removeLayer(train);
            // map.removeLayer(districtcapital);
        }
    })




// var baseMaps = {
//     "Grayscale": grayscale,
//     "Streets": streets
// };





// var testData , heatmapLayer
//  $.get('/mapapp/heatmap/', function(data) {
            
//      testData = {
//       max: 8,
//       data: data
//     };

//     var cfg = {
//   // radius should be small ONLY if scaleRadius is true (or small radius is intended)
//   // if scaleRadius is false it will be the constant radius used in pixels
//   "radius": 2,
//   "maxOpacity": .8,
//   // scales the radius based on map zoom
//   "scaleRadius": true,
//   // if set to false the heatmap uses the global maximum for colorization
//   // if activated: uses the data maximum within the current map boundaries
//   //   (there will always be a red spot with useLocalExtremas true)
//   "useLocalExtrema": true,
//   // which field name in your data represents the latitude - default "lat"
//   latField: 'lat',
//   // which field name in your data represents the longitude - default "lng"
//   lngField: 'lng',
//   // which field name in your data represents the data value - default "value"
//   valueField: 'count'
// };


// heatmapLayer = new HeatmapOverlay(cfg);
// heatmapLayer.setData(testData);
//     // $('#results_container').html(data);
//   });



