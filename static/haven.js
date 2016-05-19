/**
 * Created by aislingdempsey on 5/16/16.
 */

//this script relies on jquery
function displayResults(result){
    console.log('calling display results');
    var offset = result['offset'];
    // var total = result['total_results'];
    console.log(result);
    var businesses = result['businesses'];
    console.log(businesses);
    var term = result['term'];
    console.log($('#search-results'));
    $('#search-results').empty();

    //if something breaks, this is probably why

    //todo add link to result
    for (var yelp_id in businesses){
        console.log(yelp_id);
        var name = businesses[yelp_id]['name'];
        var category = businesses[yelp_id]['category'];

        var address1 = businesses[yelp_id]['address_line_1'] || undefined;
        var address2 = businesses[yelp_id]['address_line_2']  || undefined;
        
        var yelpRating = businesses[yelp_id]['yelp_score'];
        var havenRating = businesses[yelp_id]['score'];
        var havenCount = businesses[yelp_id]['total_ratings'];
        console.log(havenCount)
        var photo = businesses[yelp_id]['photo'];


        var container = $("<div>");
            container.attr(
                "class", "result");
            
        var image = $("<img>");
            image.attr({
                src: photo,
                class: "result-photos"
            });
        $('.result').append(image);

        var result_name = $('<p>');
            result_name.attr(
                'class', "result-name")
                .html(name);
        $('.result').append(result_name);

        if (address1 !== undefined){
            var streetAddress1 = $('<p>');
                streetAddress1.attr(
                    'class' ,"street-1")
                    .html(address1);
            $('.result').append(streetAddress1);
        }

        if (address2 !== undefined) {
            var streetAddress2 = $('<p>');
            streetAddress2.attr(
                'class', "street-2")
                .html(address2);

            $('.result').append(streetAddress2);
        }

            var yelpScore = $('<p>');
                yelpScore.attr(
                    "class", 'yelp-score')
                    .html(yelpRating);
            $('.result').append(yelpScore);

        var haven = $('<p>');
            haven.attr(
                'class', 'haven-rating')
                .html(havenRating + " out of " +  havenCount + " ratings");

        $('.result').append(haven);

        $('#search-results').append(container)

    }

    var btn = $('<button>');
        btn.attr({
            'class': 'search-more-btn',
            'data-term': term,
            'data-offset': offset}).append("More results...");
        $('#search-results').append(btn);


}

function moreResults(evt) {
    // console.log('yooooooo');
    var input = {'term': $(this).data("term"),
                'offset': $(this).data("offset")
                };
    $.get("/results.json", input, displayResults);

}


$(document).on('click', '.search-more-btn', moreResults);
