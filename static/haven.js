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
                .html("Address: <br>"+ address1);
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
            .html("Yelp has rated this as "+ yelpRating);
        $('#result-block'+resultNum).append(yelpScore);


        if (havenRating !== undefined) {
            var haven = $('<p>');

            haven.attr(
                'class', 'haven-rating')
                .html("Haven users scored this as "+ havenRating + " out of 5 over " + havenCount + " ratings");

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


window.markers=[];

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
    window.map = new google.maps.Map(document.getElementById('results-map')||document.getElementById('splash-map'), myOptions);
    //todo get smaller pin
    var image = '/static/pins/home-pin.png';
    var locGuess = new google.maps.Marker({
                    map: map,
                    draggable: true,
                    animation: google.maps.Animation.DROP,
                    position: initialLocation
                    // icon: image
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
        donut()
    }


    // // CHART
    function donut(){
        console.log('donuts called');
        var parents = {};
        var parentsArray = [];

        //**************************************************************************************************************
        //parents format=== {parent cat:{'value': number of markers, 'markers': array of markers, 'label': displayname}}
        //**************************************************************************************************************

        for (var m = 0; m < markers.length; m++) {
            //loops through markers and adds all parent categories to an array
            var marker = markers[m];

            for (var p = 0; p < marker.pcats.length; p++) {
                var parentCat = marker.pcats[p];


                // console.log(markers[i].pcats.length);
                console.log('marker:', marker);
                console.log('marker pcat:', parentCat);
                //pushes parent cat in marker pcat list to parents Array
                // parentsArray.push(markers[marker].pcats[parentCat]);
                // console.log("parentsArray:", parentsArray);




                //if parents[parentCat] doesn't exist, adds marker:

                if (parents[parentCat] === undefined) {
                    parents[parentCat] = {
                        'markers': [marker],
                        'count': 1,
                        'subCats': {}
                    };
                    console.log('Parent Category:', parentCat, "created");
                    console.log(parents[parentCat])
                }

                else{
                    parents[parentCat]['markers'].push(marker);
                    parents[parentCat]['count'] += 1;
                    console.log('Parent Category:', marker[parentCat], 'Updated') ;
                    console.log(parents[marker[parentCat]])
                }

                console.log('Parent heading into subcats:', marker[parentCat]);
                console.log('Parents OL heading into subcats:', parents);




                //
                //     //adds marker to marker array for the pcat
                //     console.log('adding to parent marker array');
                //     console.log('parent marker array:', parents[markers[marker].pcats[parentCat]]['markers']);
                //     parents[markers[marker].pcats[parentCat]]['markers'].push(markers[marker]);
                //     parents[markers[marker].pcats[parentCat]]['count'] += 1;
                //
                //
                //
                //     //makes the pcat object literal and adds a key of markers that is equal to an array of all makers
                //     //that have it
                //
                // //    if parents[parentCat] does exist:
                // } else {
                //
                //
                //
                //
                //     console.log('creating parent object and marker array');
                //     //parents[parentCat] = {'markers': [marker]
                //     parents[markers[marker].pcats[parentCat]] = {'markers': [markers[marker]],
                //                                                 'count': 1};
                //
                //
                //
                // }
                // console.log('parents before subcats:', parents);

                for (var s = 0; s < marker.cats.length; s++)
                    var subCat = marker.cats[s]

                    if (parents[parentCat]['subCats'][subCat] === undefined) {
                        parents[parentCat]['subCats'][subCat] = {
                            'markers': [marker],
                            'count': 1
                        };
                    }

                    else {
                        parents[parentCat]['subCats'][subCat]['markers'].push(marker);
                        parents[parentCat]['subCats'][subCat]['count'] += 1
                    }

                    //
                    //     parents[markers[marker].pcats[parentCat]][markers[marker].cats[subCat]] = {
                    //         'markers': [markers[marker]],
                    //         'count': 1
                    //     }
                    // }
                    // else{
                    //     parents[markers[marker].pcats[parentCat]][markers[marker].cats[subCat]]['markers']
                    //         .push(markers[marker]);
                    //     parents[markers[marker].pcats[parentCat]][markers[marker].cats[subCat]]['count'] += 1
                    // }
            }
        }
        console.log('parents', parents);
        // window.vals = [];
        // window.labls = [];
        //
        // for (var cat in parents){
        //     // console.log('parents[cat]', parents[cat]);
        //     //sets pcat['value'] to the number of markers that have it and pushes to global array
        //     parents[cat]['value'] = parents[cat]['markers'].length;
        //     vals.push(parents[cat]['value']);
        //
        //     //sets pcat['label'] to the name of the pcat and pushes it to the global array
        //     parents[cat]['label'] = cat;
        //     labls.push(parents[cat]['label']);
        //     // console.log('parents[cat].length:', parents[cat]['value']);
        //
        //     // console.log('subcat:', parents[cat]['value']);
        //     parents[cat]['label'] = cat;
        //     // console.log
        // }

        var parentSeries = [{
            name: 'Business Types',
            colorByPoint: true,
            data:[]
        }];

        var parentDrilldown = {
            series: []
        };

        for(var parentCat in parents) {
            parentSeries[0]['data'].push({
                'name': parentCat,
                'y': parents[parentCat]['count'],
                'drilldown': parentCat,
                'markers': parentCat['markers']
            });

            var subData = [];
            var cat = subCat
            for(var sc in parents[parentCat]['subCats']) {
                var subCat = parents[parentCat]['subCats'][sc];
                subData.push([sc, subCat['count']]);


                parentDrilldown['series'].push({
                    'name': parentCat,
                    'id': parentCat,
                    'data': subData,
                    'markers': subCat['markers']
                })
            }
            console.log('parentSeries:', parentSeries);
            console.log('parentDrilldown:', parentDrilldown);
        }





        $('#results-chart').highcharts({
                chart: {
                    type: 'pie'
                },
                title: {
                    text: 'Best Businesses Near You'
                },
                subtitle: {
                    text: 'Click the slices to view versions. Source: netmarketshare.com.'
                },
                plotOptions: {
                    series: {
                        dataLabels: {
                            enabled: true,
                            format: '{point.name}: {point.y}'
                        }
                    }
                },

                tooltip: {
                    headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
                    pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
                },

                series: parentSeries,
                drilldown: parentDrilldown

            });
                //



                //     data: [{
                //         name: 'Microsoft Internet Explorer',
                //         y: 56.33,
                //         drilldown: 'Microsoft Internet Explorer'
                //     }, {
                //         name: 'Chrome',
                //         y: 24.03,
                //         drilldown: 'Chrome'
                //     }, {
                //         name: 'Firefox',
                //         y: 10.38,
                //         drilldown: 'Firefox'
                //     }, {
                //         name: 'Safari',
                //         y: 4.77,
                //         drilldown: 'Safari'
                //     }, {
                //         name: 'Opera',
                //         y: 0.91,
                //         drilldown: 'Opera'
                //     }, {
                //         name: 'Proprietary or Undetectable',
                //         y: 0.2,
                //         drilldown: null
                //     }]
                // }],
                // drilldown: {
                //     series: [{
                //         name: 'Microsoft Internet Explorer',
                //         id: 'Microsoft Internet Explorer',
                //         data: [
                //             ['v11.0', 24.13],
                //             ['v8.0', 17.2],
                //             ['v9.0', 8.11],
                //             ['v10.0', 5.33],
                //             ['v6.0', 1.06],
                //             ['v7.0', 0.5]
                //         ]
                //     }, {
                //         name: 'Chrome',
                //         id: 'Chrome',
                //         data: [
                //             ['v40.0', 5],
                //             ['v41.0', 4.32],
                //             ['v42.0', 3.68],
                //             ['v39.0', 2.96],
                //             ['v36.0', 2.53],
                //             ['v43.0', 1.45],
                //             ['v31.0', 1.24],
                //             ['v35.0', 0.85],
                //             ['v38.0', 0.6],
                //             ['v32.0', 0.55],
                //             ['v37.0', 0.38],
                //             ['v33.0', 0.19],
                //             ['v34.0', 0.14],
                //             ['v30.0', 0.14]
                //         ]
                //     }, {
                //         name: 'Firefox',
                //         id: 'Firefox',
                //         data: [
                //             ['v35', 2.76],
                //             ['v36', 2.32],
                //             ['v37', 2.31],
                //             ['v34', 1.27],
                //             ['v38', 1.02],
                //             ['v31', 0.33],
                //             ['v33', 0.22],
                //             ['v32', 0.15]
                //         ]
                //     }, {
                //         name: 'Safari',
                //         id: 'Safari',
                //         data: [
                //             ['v8.0', 2.56],
                //             ['v7.1', 0.77],
                //             ['v5.1', 0.42],
                //             ['v5.0', 0.3],
                //             ['v6.1', 0.29],
                //             ['v7.0', 0.26],
                //             ['v6.2', 0.17]
                //         ]
                //     }, {
                //         name: 'Opera',
                //         id: 'Opera',
                //         data: [
                //             ['v12.x', 0.34],
                //             ['v28', 0.24],
                //             ['v27', 0.17],
                //             ['v29', 0.16]
                //         ]
                //     }]
                // }
            // });


        // var options = {responsive: true};
        //
        // var ctx = $("#resultChart");
        //
        // var chartData = {
        //     labels: labls,
        //     datasets: [
        //         {data: vals,
        //         backgroundColor: [
        //             'rgba(255, 99, 132, 0.2)',
        //             'rgba(54, 162, 235, 0.2)',
        //             'rgba(255, 206, 86, 0.2)',
        //             'rgba(75, 192, 192, 0.2)',
        //             'rgba(153, 102, 255, 0.2)',
        //             'rgba(255, 159, 64, 0.2)']
        //     }]
        //
        // }
        //
        // var myDonutChart = new Chart(ctx, {
        //     type: 'doughnut',
        //     data= chartData,
        //     options: options
        // });
        // $('#donutLegend').html(myDonutChart.generateLegend());

    }

}
//
// $(function () {
//             // Create the chart
//             $('#results-chart').highcharts({
//                 chart: {
//                     type: 'pie'
//                 },
//                 title: {
//                     text: 'Browser market shares. January, 2015 to May, 2015'
//                 },
//                 subtitle: {
//                     text: 'Click the slices to view versions. Source: netmarketshare.com.'
//                 },
//                 plotOptions: {
//                     series: {
//                         dataLabels: {
//                             enabled: true,
//                             format: '{point.name}: {point.y:.1f}%'
//                         }
//                     }
//                 },
//
//                 tooltip: {
//                     headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
//                     pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
//                 },
//                 series: [{
//                     name: 'Brands',
//                     colorByPoint: true,
//                     data: [{
//                         name: 'Microsoft Internet Explorer',
//                         y: 56.33,
//                         drilldown: 'Microsoft Internet Explorer'
//                     }, {
//                         name: 'Chrome',
//                         y: 24.03,
//                         drilldown: 'Chrome'
//                     }, {
//                         name: 'Firefox',
//                         y: 10.38,
//                         drilldown: 'Firefox'
//                     }, {
//                         name: 'Safari',
//                         y: 4.77,
//                         drilldown: 'Safari'
//                     }, {
//                         name: 'Opera',
//                         y: 0.91,
//                         drilldown: 'Opera'
//                     }, {
//                         name: 'Proprietary or Undetectable',
//                         y: 0.2,
//                         drilldown: null
//                     }]
//                 }],
//                 drilldown: {
//                     series: [{
//                         name: 'Microsoft Internet Explorer',
//                         id: 'Microsoft Internet Explorer',
//                         data: [
//                             ['v11.0', 24.13],
//                             ['v8.0', 17.2],
//                             ['v9.0', 8.11],
//                             ['v10.0', 5.33],
//                             ['v6.0', 1.06],
//                             ['v7.0', 0.5]
//                         ]
//                     }, {
//                         name: 'Chrome',
//                         id: 'Chrome',
//                         data: [
//                             ['v40.0', 5],
//                             ['v41.0', 4.32],
//                             ['v42.0', 3.68],
//                             ['v39.0', 2.96],
//                             ['v36.0', 2.53],
//                             ['v43.0', 1.45],
//                             ['v31.0', 1.24],
//                             ['v35.0', 0.85],
//                             ['v38.0', 0.6],
//                             ['v32.0', 0.55],
//                             ['v37.0', 0.38],
//                             ['v33.0', 0.19],
//                             ['v34.0', 0.14],
//                             ['v30.0', 0.14]
//                         ]
//                     }, {
//                         name: 'Firefox',
//                         id: 'Firefox',
//                         data: [
//                             ['v35', 2.76],
//                             ['v36', 2.32],
//                             ['v37', 2.31],
//                             ['v34', 1.27],
//                             ['v38', 1.02],
//                             ['v31', 0.33],
//                             ['v33', 0.22],
//                             ['v32', 0.15]
//                         ]
//                     }, {
//                         name: 'Safari',
//                         id: 'Safari',
//                         data: [
//                             ['v8.0', 2.56],
//                             ['v7.1', 0.77],
//                             ['v5.1', 0.42],
//                             ['v5.0', 0.3],
//                             ['v6.1', 0.29],
//                             ['v7.0', 0.26],
//                             ['v6.2', 0.17]
//                         ]
//                     }, {
//                         name: 'Opera',
//                         id: 'Opera',
//                         data: [
//                             ['v12.x', 0.34],
//                             ['v28', 0.24],
//                             ['v27', 0.17],
//                             ['v29', 0.16]
//                         ]
//                     }]
//                 }
//             });
// });



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



