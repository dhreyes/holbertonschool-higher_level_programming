// Write a Javascript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All move titles must be list in the HTML tag UL#list_movies
// Cannot use document.querySelector() to select the HTML tag
// Must use JQuery API
$(document).ready(function () {
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
        $.each(data.results, function (i, field) {
            $("#list_movies").append("<li>" + field.title + "</li>");
        });
    });
}
);
