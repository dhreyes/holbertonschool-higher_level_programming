// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character_name
// Cannot use document.querySelector() to select HTML tag
// Must use the JQUERY API
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
    $('#character_name').text(data.name);
}
);