/**
 * Created by aislingdempsey on 5/16/16.
 */

//this script relies on jquery
function displayResults(result) {
    console.log('calling display results');
    var offset = result['offset'];
    // var total = result['total_results'];
    console.log(result);
    var businesses = result['businesses'];
    console.log(businesses);
    var term = result['term'];
    var sort = result['sort'];
    var cutoff = result['cutoff'];
    $('#search-results').empty();
    
    var resultNum = 1;
    for (var yelp_id in businesses) {
        console.log(yelp_id);
        var name = businesses[yelp_id]['name'];
        var category = businesses[yelp_id]['category'];

        var address1 = businesses[yelp_id]['address_line_1'] || undefined;
        var address2 = businesses[yelp_id]['address_line_2'] || undefined;

        var yelpRating = businesses[yelp_id]['yelp_score'];
        var havenRating = businesses[yelp_id]['score'] + 2|| undefined;
        var havenCount = businesses[yelp_id]['total_ratings'];
        console.log(havenCount);
        var photo = businesses[yelp_id]['photo'];


        var container = $("<div>");
        container.attr(
            "id", "result" + resultNum);
        $('#search-results').append(container);

        var image = $("<img>");
        image.attr({
            src: photo,
            class: "result-photos"
        });
        $('#result'+resultNum).append(image);

        var link =$('<a>');
            link.attr({
            href: "/info/"+yelp_id,
            id: "bus-link"+resultNum
        });
        $('#result'+resultNum).append(link);

        var result_name = $('<p>');
        result_name.attr(
            'class', "result-name")
            .html(name);
        $('#bus-link'+resultNum).html(name);

        if (address1 !== undefined) {
            var streetAddress1 = $('<p>');
            streetAddress1.attr(
                'class', "street-1")
                .html(address1);
            $('#result'+resultNum).append(streetAddress1);
        }

        if (address2 !== undefined) {
            var streetAddress2 = $('<p>');
            streetAddress2.attr(
                'class', "street-2")
                .html(address2);

            $('#result'+resultNum).append(streetAddress2);
        }


        var yelpScore = $('<p>');
        yelpScore.attr(
            "class", 'yelp-score')
            .html(yelpRating);
        $('#result'+resultNum).append(yelpScore);


        if (havenRating !== undefined) {
            var haven = $('<p>');

            haven.attr(
                'class', 'haven-rating')
                .html(havenRating + " out of " + havenCount + " ratings");

            $('#result' + resultNum).append(haven);
        }

        if (havenRating == undefined) {
            var haven = $('<p>');

            haven.attr(
                'class', 'haven-rating')
                .html("Nobody has rated this business yet. Be the first!");

            $('#result' + resultNum).append(haven);
        }

        resultNum ++

    }

    console.log($("#search-results div").length);
    if ($("#search-results div").length === 10){
        var btn = $('<button>');
            btn.attr({
                'class': 'search-more-btn',
                'data-term': term,
                'data-offset': offset,
                'data-sort': sort,
                'data-cutoff': cutoff}).append("More results...");
            $('#search-results').append(btn);}


}

function moreResults(evt) {
    // console.log('yooooooo');
    var input = {'term': $(this).data("term"),
                'offset': $(this).data("offset"),
                'sort': $(this).data("sort"),
                'cutoff': $(this).data("cutoff")
                };
    console.log('cutoff', $(this).data("cutoff"));
    $.get("/results.json", input, displayResults);

}


//event listener for rendering more results on searches
$(document).on('click', '.search-more-btn', moreResults);

function initMap(evt) {
    //sets default location to Hackbright in case html5 geolocation is not supported
    var defaultLatLong = {lat: 37.788904, lng: -122.414244487882};

    var myOptions = {zoom: 18,
        mapTypeID: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById('splash-map'), myOptions);
    //checks if geolocation is supported by the browser and
    if (navigator.geolocation) {
        var browserSupportFlag = true;
        navigator.geolocation.getCurrentPosition(function (position) {
            var initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            // console.log(initialLocation);
            map.setCenter(initialLocation);


            var locGuess = new google.maps.Marker({
                map: map,
                draggable: true,
                animation: google.maps.Animation.DROP,
                position: initialLocation
            });

            //gets best local businesses near starting point
            var geocoder = new google.maps.Geocoder;
            geocoder.geocode({location: initialLocation}, function(results){
                // console.log(results[0].formatted_address);
                getLocalBest(results[0].formatted_address);
            });

            //creates info window of geolocated address
            geocoder.geocode({location: initialLocation}, function(results){
                var current_address = results[0].formatted_address;
                var infoWindow = new google.maps.InfoWindow({
                    content: "It looks like you're located at " + current_address
                });
                infoWindow.open(map, locGuess)
            });


        }, function () {
            handleNoGeolocation(browserSupportFlag)
        });
    }




    else {
        var browserSupportFlag = false;
        handleNoGeolocation(browserSupportFlag);
    }

    function handleNoGeolocation(errorFlag) {
        if (errorFlag == true) {
          alert("Geolocation service failed.");
          var initialLocation = defaultLatLong;
        } else {
            alert("Your browser doesn't support geolocation, please enter an address");
            var initialLocation = defaultLatLong
        }
        map.setCenter(initialLocation);
    }

    //loops through json of business info and plots points on map.
    function addPins(businesses) {
    // console.log (businesses);

        var markers = [];
        for (var business in businesses) {
        // console.log(business);
        // console.log(businesses[business]);
        // console.log(businesses[business]['longitude']);
        // console.log(businesses[business]['latitude']);


            var businessInfo = '<div id="marker">' +
                '<div id="Header">'+
                    '<h3>'+
                        businesses[business]['name'] +
                    '</h3>'+
                    '</div>';



            var marker = new google.maps.Marker({
                map: map,
                draggable: false,
                animation: google.maps.Animation.DROP,
                position: {
                    lat: businesses[business]['latitude'],
                    lng: businesses[business]['longitude']
                    },
                html: businessInfo
                });

            markers.push(marker);




            var infoWindow = new google.maps.InfoWindow({
                content: "Loading..."});


            //opens closes any open info windows and opens a new one for the marker being clicked
            marker.addListener('click', function(){
                infoWindow.setContent(this.html);
                infoWindow.close();
                infoWindow.open(map, this);
            });

        }
        //instantiates the LatLngBounds class
        var newBounds = new google.maps.LatLngBounds();
        //for every marker in the markers list, extends the bounds
        $.each(markers, function(index, marker){
            newBounds.extend(marker.position)
        });

        //updates the bounds of the map to fit the points
        map.fitBounds(newBounds);
    }

    function getLocalBest(result){
        var location = {'location': result};
        $.get('/local-best.json', location, addPins)
    }




}

// function addPins(businesses) {
//     // console.log (businesses);
//     for (var business in businesses) {
//         // console.log(business);
//         // console.log(businesses[business]);
//         // console.log(businesses[business]['longitude']);
//         // console.log(businesses[business]['latitude']);
//         var marker = new google.maps.Marker({
//             map: window.map,
//             draggable: true,
//             animation: google.maps.Animation.DROP,
//             position: {
//                 lat: businesses[business]['latitude'],
//                 lng: businesses[business]['longitude']
//             }
//
//         });
//     }
// }




function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}


    // $.get"maps.googleapis.com/maps/api/geocode/json?latlng="+myLatLng['lat']+","+myLatLng['lng']+"&key="+YOUR_API_KEY
    //
    // $.get"/local.json", address, addLocalBest

google.maps.event.addDomListener(window, 'load', initMap);