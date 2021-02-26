

// Define const values in the systems
const geoserverUrl = "http://socrates.cersgis.org:8080/geoserver/cite/wms?";
const geoserverlulcUrl = "http://socrates.cersgis.org:8080/geoserver/charcoal/wms?";
const geojsonurl = 'http://boundapi.cersgis.org/'

// function addtomap(mapdiv, zoomcontrol) {
//    let mapcon =  L.map(mapdiv, {
//         minZoom: 7,
//         maxZoom: 20,
//         //maxBounds: L.latLngBounds([8.1139, -1.2272], [9.1643, 1.0220]),
//          layers: [grayscale, cities]
//         measureControl: false,
//     }).setView([6.31, -10.791], 12);
//    return mapcon
// }

// Refresh map state 
function maprefresh() {
   if (map) {
       map.invalidateSize();
   }
}



function loadVectorlayerfunction(url, layername, check) {
   let loaddata;
   loaddata = L.tileLayer.wms(url, {
       layers: 'cite:' + layername,
       format: 'image/png',
       transparent: true,

   }); {
    if (check) { map.addLayer(loaddata) }
    } 
   return loaddata;
}





function layerTogglefunction(map, layername, checkbox) {
    if (layername) {
        if (checkbox.prop('checked') == false) {
            map.removeLayer(layername);
        } else {
            map.addLayer(layername);
        }
    } else {
        alert('Layer not is ready for visualisation.');
        checkbox.prop('checked', false)
    }
}

// function layerClick(map, layername, checkbox) {
//     if (layername) {
//         if (checkbox.prop('checked') == false) {
//             map.removeLayer(layername);
//         } else {
//             map.addLayer(layername);
//         }
//     } else {
//         alert('Layer not is ready for visualisation.');
//         checkbox.prop('checked', false)
//     }
// }

function sliderfunct(rangevalue, tilelayer){
  rangevalue == 0 ? tilelayer.setOpacity(0) : tilelayer.setOpacity(rangevalue / 10);
  tilelayer.setParams({}, false)
  return rangevalue
}


function sliderTogglefunction(slider, value) {
       if (value == false) {
           $(slider).addClass('hidden');
       } else {
           $(slider).removeClass('hidden');
       }
 }



function geoprotect(url, geodata, style, onEachFeature) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, { style: style, onEachFeature: onEachFeature });
        geodata.bringToBack();

        // $(check).on('change', function(e){
        //   layerTogglefunction(map, geodata, $(this));
        // });

    })

    return geodata
}






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




 function layerseldefine(mapm, layername, layername1) {
  if (layername1){
    mapm.removeLayer(layername1);
  }
   mapm.addLayer(layername);
   layername1 = layername
   return layername1
}



function removearray(array, itemtoremove ){
  array.splice($.inArray(itemtoremove, array),1);
}


function geojsonloadpoint(url, geodatas, style, onEachFeature, check) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {

        geodatas = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {

             

               
                return L.circleMarker(latlng, style);
                
            },
            onEachFeature: onEachFeature
        });
        geodatas.bringToBack();
        if (check) { map.addLayer(geodatas) }
    })

    return geodatas
}
