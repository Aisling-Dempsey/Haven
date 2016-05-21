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
    //todo add link to result
    for (var yelp_id in businesses) {
        console.log(yelp_id);
        var name = businesses[yelp_id]['name'];
        var category = businesses[yelp_id]['category'];

        var address1 = businesses[yelp_id]['address_line_1'] || undefined;
        var address2 = businesses[yelp_id]['address_line_2'] || undefined;

        var yelpRating = businesses[yelp_id]['yelp_score'];
        var havenRating = businesses[yelp_id]['score'] || undefined;
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


$(document).on('click', '.search-more-btn', moreResults);
