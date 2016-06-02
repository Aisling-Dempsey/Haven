/**
 * Created by aislingdempsey on 5/16/16.
 */

var callStack = [];

function displayBusiness(result){
    var name = result.yelp_bus_data.name;

    var categories = result.categories;

    var busAddressArray = result.yelp_bus_data.location.display_address || undefined;

    var coords ={};
    coords.lat = result.yelp_bus_data.location.coordinate.latitide;
    coords.lng = result.yelp_bus_data.location.coordinate.longitude;

    var phone = result.yelp_bus_data.display_phone || undefined;

    //replaces with larger version of image
    var image = result.yelp_bus_data.image_url.replace('/ms.jpg', '/l.jpg')

    var recentReview = result.recent_review || undefined;

    var recentScore = result.recent_score || undefined;

    var score = result.score + 3 || undefined;
    console.log('result.score:', result.score);
    console.log('score:', score);
    var totalRatings = result.total_ratings || undefined;

    var yelpUrl = result.yelp_bus_data.url;

    var userRating = result.user_rating || undefined;
    console.log ('userRating:', userRating);
    if (userRating != undefined) {
        var userScore = userRating.score || undefined;

        var createdAt = userRating.created_at || undefined;

        var userReview = userRating.review || undefined;

        var userRatingId = userRating.rating_id || undefined;
    }
    var yelpScore = result.yelp_bus_data.rating || undefined;

    var yelpReviewImg = result.yelp_bus_data.snippet_image_url || undefined;

    var yelpReviewTxt = result.yelp_bus_data.snippet_text || undefined;

    var yelpId = result.yelp_bus_data.id;


    //empties div
    $('#search-results').empty();

    var businessBlock = $('<div>');
        businessBlock.attr({
            class: 'row',
            id: 'bus-block'
        });
    $('#search-results').append(businessBlock);

    var busInfo = $('<div>');
        busInfo.attr({
            class: 'busInfo col-lg-10 col-lg-offset-1',
            id: 'bus-info'});
    $('#bus-block').append(busInfo);

    var busRow = $('<div>');
        busRow.attr({
            class: 'row',
            id: 'bus-row'
        });
    $('#bus-info').append(busRow);

    var busInfoBlock = $('<div>');
        busInfoBlock.attr({
            class: 'col-lg-9',
            id: 'bus-info-block'
        });
    $('#bus-row').append(busInfoBlock);

    var mapBlock = $('<div>');
        mapBlock.attr({
            class: 'col-lg-3 map',
            id: 'solo-bus-map'
        });
    $('#bus-row').append(mapBlock);
    var busInfoRow = $('<div>');
        busInfoRow.attr({
            class: 'row',
            id: 'bus-info-row'
        });
    $('#bus-info-block').append(busInfoRow);

    var photoDiv = $('<div>');
        photoDiv.attr({
            class: 'col-lg-4',
            id: "solo-bus-photo-div"
        });
    $('#bus-info-row').append(photoDiv);

    var soloBusPhoto = $('<img>');
        soloBusPhoto.attr({
            src: image,
            class: 'img-responsive',
            id: 'solo-bus-photo'
        });
    $('#solo-bus-photo-div').append(soloBusPhoto);


    var busTextBlock = $('<div>');
        busTextBlock.attr({
            class: 'col-lg-8',
            id:"bus-text-block"
        });
    $('#bus-info-row').append(busTextBlock);

    var busTopRow = $('<div>');
        busTopRow.attr({
            class: 'row',
            id: 'bus-top-row'
        });
    $('#bus-text-block').append(busTopRow);

    var soloBusUrl= $('<a>');
        soloBusUrl.attr({
            class: 'col-lg-6',
            id: 'solo-bus-url',
            href: yelpUrl
        });
    $('#bus-top-row').append(soloBusUrl);

    var busName = $('<p>');
        busName.attr({
            id: 'solo-bus-name'
        }).append(name);
    $('#solo-bus-url').append(busName);

    var busAggrRating = $('<p>');
        busAggrRating.attr({
            class: 'col-lg-6',
            id: 'bus-aggr-rating'
        });
        if(score !== undefined){
            busAggrRating.append('Haven score: '+ score)
        }
        else{
            busAggrRating.append('Haven score: '+ 'No ratings yet')
        }
    $('#bus-top-row').append(busAggrRating);

    var bus2ndRow = $('<div>');
        busTopRow.attr({
            class: 'row',
            id: 'bus-2nd-row'
        });
    $('#bus-text-block').append(bus2ndRow);


    var busPhone = $('<p>');
        busPhone.attr({
            class: 'col-lg-6',
            id: "solo-bus-phone"
        }).append(phone);
    $('#bus-2nd-row').append(busPhone);

    var soloYelpScore = $('<p>') ;
        soloYelpScore.attr({
            class: 'col-lg-6',
            id: 'solo-yelp-rating'
        }).append('Yelp score: ' + yelpScore);
    $('#bus-2nd-row').append(soloYelpScore);

    var bus3rdRow = $('<p>');
        bus3rdRow.attr({
            class: 'row',
            id: 'bus-3rd-row'
        });
     $('#bus-text-block').append(bus3rdRow);



    var busAddress = $('<p>');
        busAddress.attr({
            class: 'col-lg-6',
            id: 'solo-bus-address'
        });
        var formattedAddress ='';
        for(var i=0; i < busAddressArray.length; i++){
            formattedAddress += busAddressArray[i] + '<br>'
            }
        busAddress.append(formattedAddress);
    $('#bus-3rd-row').append(busAddress);
    
    var reviewsBlockRow = $('<div>');
        reviewsBlockRow.attr({
            class: 'row',
            id: 'reviews-block-row'
        });
    $('#search-results').append(reviewsBlockRow);
    
    var havenReviewsBlock = $('<div>');
        havenReviewsBlock.attr({
            class: 'col-lg-6',
            id: 'haven-review-block'
        });
    $('#reviews-block-row').append(havenReviewsBlock);



    var yelpReviewsBlock = $('<div>');
        yelpReviewsBlock.attr({
            class: 'col-lg-6',
            id: 'yelp-review-block'
        });
    $('#reviews-block-row').append(yelpReviewsBlock);
    

    
    var havenRow1 = $('<div>');
        havenRow1.attr({
            class: 'row',
            id: 'haven-row-1'
        });
    $('#haven-review-block').append(havenRow1);

    var havenTitleDiv = $('<div>');
        havenTitleDiv.attr({
           class: 'col-lg-12',
            id: 'haven-title-div'
        });
    $('#haven-row-1').append(havenTitleDiv);

    var havenTitle = $('<h3>');
        havenTitle.attr({
            id: 'haven-title'
        }).append('Haven says:');
    $('#haven-title-div').append(havenTitle);

    var havenRow2 = $('<div>');
        havenRow2.attr({
            class: 'row',
            id: 'haven-row-2'
        });
    $('#haven-review-block').append(havenRow2);

    var havenReviewsDiv = $('<h3>');
        havenReviewsDiv.attr({
            class: 'col-lg-12',
            id: 'haven-reviews-div'
        });
    $('#haven-row-2').append(havenReviewsDiv);

    // if (recentScore !== undefined){
    //     var havenRecentScore = $('<p>');
    //     havenRecentScore.attr({
    //
    //     })
    // }
    //
    // if (recentReview !== undefined){
    //     var recentReviewText = $('<p>');
    //         recentReviewText.attr(
    //             class: 'col-lg-12'
    //             id: 'haven-review-text'
    //         )
    // }



    var havenRow3 = $('<div>');
        havenRow3.attr({
            class: 'row',
            id: 'haven-row-3'
        });
    $('#haven-review-block').append(havenRow3);

    var havenModalReviewBtn = $('<button>');
        havenModalReviewBtn.attr({
           class: 'col-lg-8 col-lg-offset-2',
            id: 'haven-review-modal-btn',
            'data-name': name,
            'data-userScore': userScore,
            'data-userReview': userReview,
            'data-created-at': createdAt,
            'data-yelpID': yelpId,
            'data-userRatingId': userRatingId
        }).append('Review Me');
    $('#haven-row-3').append(havenModalReviewBtn);

    var backBtn = $('<button>');
        backBtn.attr({
            class: 'col-lg-2 col-lg-offset-5',
            id: 'return-to-query-btn',
            'data-term': callStack.slice(-1)[0]['term'],
            'data-offset': callStack.slice(-1)[0]['offset'],
            'data-sort': callStack.slice(-1)[0]['sort'],
            'data-cutoff': callStack.slice(-1)[0]['cutoff']
        }).append('Return to Business Results');
    $('#bus-block').append(backBtn);

//    todo build event listener to handle click

    $('#haven-review-modal-btn').click(reviewBox);
    $('#return-to-query-btn').click(moreResults)

}
//
function reviewBox(evt){
    $('#myModal').modal({
        keyboard: false
    });
    var yelpId = $(this).data('yelpid');
    var name = $(this).data('name');
    var createdAt = $(this).data('created-at') || undefined;
    var userScore = $(this).data('userscore') || undefined;
    var userReview = $(this).data('userreview') || undefined;
    var ratingId = $(this).data('userratingid') || undefined;
    if (userScore == undefined){
        var buttonText = "Submit Rating";
        var headingText = "Rate " + name
    }
    else{
        var buttonText = "Update your Rating";
        var headingText = "Your review from " + createdAt
    }


    $('#modal-title').html(headingText);
    $('.modal-body').html("" +
        "<form> " +
        "<label>Score" +
            "<select name='score' id='user-score-selection' required> " +
            "<!--keeps dropdown blank to prevent accidental scoring--> " +
                "<option selected disabled hidden style='display: none' value=''>" +
                "</option> <option value='-2'>1</option> " +
                "<option value='-1'>2</option> " +
                "<option value='0'>3</option> " +
                "<option value='1'>4</option> " +
                "<option value='2'>5</option> " +
            "</select> " +
        "</label> " +
        "<label>" +
            "<p>Review (500 chars max):</p>" +
        "</label> " +
            "<div id='review-box'>" +
                "<textarea id='user-review-box' name='review' placeholder='Enter your review here' maxlength='500'>" +
                "</textarea>" +
            "</div>" +
        "</label>" +
        "</form>");

    if (userReview != undefined){
        console.log('review should be entered');
        console.log(userReview);
        $('#user-review-box').append(userReview)
    }
    if (userScore !== undefined){
        console.log('score should be entered');
        $('#user-score-selection').val(userScore)
    }

    $('.modal-footer').html('<button type="button" class="btn btn-primary" data-dismiss="modal" data-yelpID="' +yelpId +
        '" data-rating-id="' + ratingId + '" id="review-submit-btn">'+ buttonText + '</button>');

    $('#myModal').modal('show');

    function updateReview(evt){
        var yelpId = $(this).data('yelpid');
        var score = $('#user-score-selection').val();
        var review = $('#user-review-box').val();
        var ratingId =$(this).data('rating-id');
        console.log(yelpId)

        var input = {'yelp_id': yelpId,
                    'score': score};

        console.log('event handler triggered');
        if (review !== ''){
            input['review'] = review;
            console.log('has a review')
        }

        if (typeof(score) === 'string'){
            //updates prior rating if it exists
            if (ratingId !== 'undefined'){
                input['rating_id'] = ratingId;
                console.log('updated rating');}
            $.post('/info/'+yelpId+'/rate', input, function(){console.log('review updated successfully')});

            console.log('should post')
        }

        else{
            console.log("no score, shouldn't post")
        }

    }


    $('#review-submit-btn').click(updateReview)



    ;
}

//this script relies on jquery
function displayResults(result) {
    // console.log('calling display results');
    var offset = result['offset'];
    // var total = result['total_results'];
    console.log('result:', result);
    var businesses = result['businesses'];
    // console.log(businesses);
    var term = result['term'];
    var sort = result['sort'];
    var cutoff = result['cutoff'];
    $('#search-results').empty();

    var map = $("<div>");
    map.attr("id", "results-map");
    $('#search-results').append(map);
    $('#search-results').addClass('container');

    initMap(result['businesses']);


    var resultNum = 1;
    for (var yelp_id in businesses) {
        // console.log(yelp_id);
        var name = businesses[yelp_id]['name'];
        var category = businesses[yelp_id]['category'];

        var address1 = businesses[yelp_id]['address_line_1'] || undefined;
        var address2 = businesses[yelp_id]['address_line_2'] || undefined;

        var yelpRating = businesses[yelp_id]['yelp_score'];
        var havenRating = businesses[yelp_id]['score']|| undefined;
        var havenCount = businesses[yelp_id]['total_ratings'];
        // console.log(havenCount);
        var photo = businesses[yelp_id]['photo'];


        var result = $("<div>");
        result.attr({
                id: "result" + resultNum,
                class: "query-result row"});
        $('#search-results').append(result);

        var resultBlock = $("<div>");
            resultBlock.attr({
                class: "query-block col xs-12 l-8 l-offset-4",
                id: "result-block" + resultNum});
        $('#result'+resultNum).append(resultBlock);


        var image = $("<img>");
        image.attr({
                src: photo,
                class: "result-photos col"
        });
        $('#result-block'+resultNum).append(image);

        var link =$('<a>');
            link.attr({
                href: "/info/"+yelp_id+".json",
                class: "bus-link",
                id: "bus-link"+resultNum
        });
        $('#result-block'+resultNum).append(link);

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
            $('#result-block'+resultNum).append(streetAddress1);
        }

        if (address2 !== undefined) {
            var streetAddress2 = $('<p>');
            streetAddress2.attr(
                'class', "street-2")
                .html(address2);

            $('#result-block'+resultNum).append(streetAddress2);
        }


        var yelpScore = $('<p>');
        yelpScore.attr(
            "class", 'yelp-score')
            .html(yelpRating);
        $('#result-block'+resultNum).append(yelpScore);


        if (havenRating !== undefined) {
            var haven = $('<p>');

            haven.attr(
                'class', 'haven-rating')
                .html(havenRating + " out of " + havenCount + " ratings");

            $('#result-block' + resultNum).append(haven);
        }

        if (havenRating == undefined) {
            var haven = $('<p>');

            haven.attr(
                'class', 'haven-rating')
                .html("Nobody has rated this business yet. Be the first!");

            $('#result-block' + resultNum).append(haven);
        }

        resultNum ++

    }
   if (callStack.length > 1){
       var mostRecent = callStack.slice(-2,-1)[0];

       var btn = $('<button>');
       btn.attr({
            'id': 'results-back-btn',
            'class': 'nav-btn',
            'data-term': mostRecent.term,
            'data-offset': mostRecent.offset,
            'data-sort': mostRecent.sort,
            'data-cutoff': mostRecent.cutoff
       }).append("<< Go back");
       $('#search-results').append(btn);
       //
       // $('#results-back-btn').click(function(evt){
       //     callStack.pop();
       //  //  todo fix always returning to first result
       //
       //     moreResults(evt)})
    }
    if ($(".query-result").length ===10){
        // var nextValues = callStack.slice(-1)[0];
        // console.log('make button called');
        var btn = $('<button>');
            btn.attr({
                'id': 'search-more-btn',
                'class': 'nav-btn',
                'data-term': term,
                'data-offset': offset,
                'data-sort': sort,
                'data-cutoff': cutoff
            }).append("More results >>");
            $('#search-results').append(btn);}


    $('.bus-link').click(renderBusiness)
}

function renderBusiness(evt){
    evt.preventDefault();
    var link = $(this).attr('href');
    console.log(link);
    $.get(link, function(result){displayBusiness(result)})
}


function moreResults(evt) {
    // console.log('yooooooo');
    //todo add scroll to return you to top
    evt.preventDefault();

    // if (back !== false){console.log('moreResults called correctly')}
    console.log("'this' is equal to:", $(this));
    var input = {'term': $(this).data("term")||$('#search-field').val(),
                //todo convert this.data to a list
                'offset': $(this).data("offset")||0,
                'sort': $(this).data("sort")||$('.sort-type:checked').val(),
                'cutoff': $(this).data("cutoff")||$('#haven-cutoff').val()
                };
    //if the button being clicked is the more results button, adds to the call stack
    if ($(this).attr('id') !== "results-back-btn"){callStack.push(input)}
    //if the button being clicked is the back button, the topmost value is removed from the callstack
    else if ($(this).attr('id') === "results-back-btn"){
        callStack.pop()}

    console.log('offset', input.offset);
    $.get("/results.json", input, displayResults);

}


//event listener for rendering more results on searches
$(document).on('click', '#search-more-btn', moreResults);
$(document).on('click', '#results-back-btn', moreResults);
$('#search-btn').click(function(evt){
    callStack.length = 0;
    moreResults(evt)
});


//*******************************
//MAPS FUNCTIONS

var subcategories={};

//global array of map markers


var markers=[];

function clearOverlays(){
    //loops through global array of markers and sets the map to null, then resets markers to an empty list
    //todo add comparison to filter-by list for what to clear

    for (var i=0; i < markers.length; i++){
        markers[i].setMap(null)
    }
    markers.length = 0;
}
//event handler to load map
function initMap(data) {
    console.log('data', data);
    // businessList = businessList || undefined;
    //sets default location to Hackbright in case html5 geolocation is not supported
    var defaultLatLong = {lat: 37.788904, lng: -122.414244487882};
    console.log('generating map');
    var myOptions = {
        zoom: 18,
        mapTypeID: google.maps.MapTypeId.ROADMAP
    };
    console.log('initial location', initialLocation);
    //makes the map equal to the results map if it exists, if not, then the splash map
    var map = new google.maps.Map(document.getElementById('results-map')||document.getElementById('splash-map'), myOptions);
    //todo get smaller pin
    var image = '/static/pins/home-pin.png';
    var locGuess = new google.maps.Marker({
                    map: map,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    position: initialLocation,
                    icon: image
                });

    console.log(locGuess);
    var infoWindow = new google.maps.InfoWindow({
        content: currentAddress
    });

    locGuess.addListener('click', function () {
        infoWindow.close();
        infoWindow.open(map, this);
    });

    // if (businessList !== undefined){
    //
    // }

    if($.isEmptyObject(data)) {
            // todo replace with modal
            console.log('There are no businesses in your area')
        }
    else{addPins(data)}
    //
    // getLocalBest(currentAddress, $('#haven-cutoff').val());
    // // alert("It looks like you're located at ".concat(current_address));

    //EVENT LISTeNER TO GET NEW BUSINESS LIST USING NEW CUTOFF VALUE
    $('#haven-cutoff').change(function (evt) {
        updateCutoff(evt);
        cutoff = $('#haven-cutoff').val();
        getLocalBest(currentAddress, cutoff, function(data){
            if($.isEmptyObject(data)){console.log('There are no businesses in your area')}
            else{
                addPins(data)
            }
        })
    });



    //loops through json of business info and plots points on map.
    function addPins(businesses) {

        clearOverlays();

        //todo add info-window using location

        // category

        for (var business in businesses) {
            // console.log(business);
            // console.log(businesses[business]);
            // console.log(businesses[business]['longitude']);
            // console.log(businesses[business]['latitude']);
            //

            var businessInfo = '<div id="marker">' +
                '<div id="Header">' +
                '<h3>' +
                businesses[business]['name'] +
                '</h3>' +
                '</div>';


            var marker = new google.maps.Marker({
                map: map,
                draggable: false,
                animation: google.maps.Animation.DROP,
                position: {
                    lat: businesses[business]['latitude'],
                    lng: businesses[business]['longitude']
                },
                html: businessInfo,
                cats: businesses[business]['cat_list'],
                pcats: []

            });
            //
            for (var i=0; i < marker.cats.length; i++)
                if (parentCats[marker.cats[i]] !== undefined){
                    // console.log($.inArray(parentCats[marker.cats[i]], marker.pcats));
                    if ($.inArray(parentCats[marker.cats[i]], marker.pcats) === parseInt(-1)){
                        marker.pcats.push(parentCats[marker.cats[i]])}
                }



            // for (var i = 0; i < businesses[business]['cat_list'].length; i++){
            //     var parent = parentCats[businesses[business]['cat_list'][i]];
            //     categories.push(parent)
            // }

            // marker.categories = for(subcategory of businesses[business]['cat_list']);

            // marker.pcats = categories;
            markers.push(marker);


            var infoWindow = new google.maps.InfoWindow({
                content: "Loading..."
            });

            // console.log(businessInfo);
            //opens closes any open info windows and opens a new one for the marker being clicked
            marker.addListener('click', function () {
                console.log(this.html);
                infoWindow.setContent(this.html);
                infoWindow.close();
                infoWindow.open(map, this);
                // var image = '/static/pins/mm_20_yellow.png';
                // this.icon = image
            });

        }
        //instantiates the LatLngBounds class
        var newBounds = new google.maps.LatLngBounds();
        //for every marker in the markers list, extends the bounds

        $.each(markers, function (index, marker) {
            newBounds.extend(marker.position)
        });

        //updates the bounds of the map to fit the points
        map.fitBounds(newBounds);
        console.log(markers);
        //
        // donut()
    }


    // // CHART
    // function donut(){
    //     console.log('donuts called');
    //     var parents = {};
    //     var parentsArray = [];
    //     for (var i = 0; i < markers.length; i++) {
    //         for (var p = 0; p < markers[i].pcats.length; p++) {
    //             console.log(markers[i].pcats.length);
    //             console.log(markers[i]);
    //             console.log(markers[i].pcats[p]);
    //             parentsArray.push(markers[i].pcats[p]);
    //             console.log("parentsArray:", parentsArray);
    //             if (parents[markers[i].pcats[p]] !== undefined) {
    //                 //intended behaviour: either append the marker to the parent, or mae it equal to an array of it.
    //                 console.log('past the if');
    //                 console.log(parents[markers[i].pcats[p]]);
    //                 parents[markers[i].pcats[p]].push(markers[i])
    //             } else {
    //                 console.log('in the else');
    //                 parents[markers[i].pcats[p]] = [markers[i]]}
    //         }
    //     }
    //     console.log(parents);
    //     for (var cat in parents){
    //         parents[cat]['value'] = parents[cat].length;
    //         console.log(parents[cat]['value']);
    //         parents[cat]['label'] = cat
    //     }
    //
    //     var options = {responsive: true};
    //
    //     var ctx_donut = $("#resultChart");
    //
    //
    //
    //     var myDonutChart = new Chart(ctx_donut, {type: 'doughnut', data: 'parents', options:'options'});
    //     $('#donutLegend').html(myDonutChart.generateLegend());
    //
    // }

}

    //gets best local businesses above cutoff
function getLocalBest(location, cutoff, callback) {
    // console.log('getLocalBest called');
    var payload = {'location': location,
        'cutoff': cutoff
    };
    $.get('/local-best.json', payload, function (data) {
        // console.log(typeof(data));
        // console.log(data);

        //todo, check if the map breaks at hackbright, this is why
        callback(data);
        // console.log('generating map');

        // addPins(data)
        // initMap(data)
    })
}


//event listener to load map on page load
// google.maps.event.addDomListener(window, 'load', initMap);

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}

// function updateChart(businesses){
//    loop through markers on click, generate dict of count

// }



//*******************************
//CUTOFF ADJUSTMENT FUNCTIONS

//event handler to update displayed cutoff above fader
function updateCutoff(evt){
    console.log('update cutoff run');
    $('#cutoff-val').html("Don't show ratings below " + (parseFloat($('#haven-cutoff').val()) + 3));

}

//event listener to update the cutoff when the fader is changed
$('#haven-cutoff').change(updateCutoff);


function getLocation(evt) {
    // console.log('getLocation called');
    if (navigator.geolocation) {
        var browserSupportFlag = true;
        // todo build if statement to check whether location has been defined.
        navigator.geolocation.getCurrentPosition(function (position) {
            window.initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            // console.log(initialLocation);

            //gets best local businesses near starting point
            var geocoder = new google.maps.Geocoder;
            // console.log('currentAddress inside getLocation', currentAddress);
             // if (currentAddress === undefined) {
                geocoder.geocode({location: initialLocation}, function (results) {
                    // console.log(results[0].formatted_address);
                    // console.log(results[0].formatted_address);
                    window.currentAddress = results[0].formatted_address;
                    // console.log(currentAddress);
                    
                    // address popup modal
                    $('#myModal').modal({
                        keyboard: false
                    });
                    $('#modal-title').html('Verify your Address');
                    $('.modal-body').html("<form><textarea id='user-address' name='initialLocation'></textarea></form>");
                    $('#user-address').val(currentAddress);

                    $('#myModal').modal('show')
                    ;
                })
            // }
                ;

            $('#save-address-btn').click(setNewAddress);

            //
            // $('#myModal').modal({
            //     keyboard: false
            // });
            //
            // $('#address').html("<form action='/set-address'><input type='text' name= 'initialLocation' placeholder= "+
            //     current_address + "><input type='submit'>");
            //
            // $('#myModal').modal('show')
            //


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
            // todo enter address for modal
            alert("Geolocation service failed.");
            window.initialLocation = defaultLatLong;
        } else {
            // todo enter address for modal
            alert("Your browser doesn't support geolocation, please enter an address");
            window.initialLocation = defaultLatLong
        }
    }
}

function setNewAddress (evt){
    window.currentAddress = $('#user-address').val();
    var address = {'address': currentAddress};
    // console.log(address);
    var geocoder = new google.maps.Geocoder();
    var cutoff = $('#haven-cutoff').val();
    geocoder.geocode(address, function(results){
       window.initialLocation= results[0].geometry.location;
        // console.log('initial location within set address', initialLocation);
        $.post('/set-address', address, function(){getLocalBest(currentAddress, cutoff,
            function(data){initMap(data)})})
    });
}

function getSession(evt){
    $.get('/get-session.json', function(results){
        userAddress = results.user_address || undefined;
        console.log(userAddress);
        if (userAddress != undefined){
            window.currentAddress = userAddress
        }
        getLocation(evt)
    })
}

$('#address-btn').click(getLocation);
// $(document).on('click', '#random-fucking-btn', function(){console.log('button')});


//todo add middle function to check for session var
$(document).ready(getLocation);


    // $.get"maps.googleapis.com/maps/api/geocode/json?latlng="+myLatLng['lat']+","+myLatLng['lng']+"&key="+YOUR_API_KEY
    //
    // $.get"/local.json", address, addLocalBest



