// Write a JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello
// Cannot use document.querySelector() to select the HTML tag
// Must use JQuery API
// The translation of "hello" must be displayed in the HTML tag DIV#hello
// Script must work when it is imported from the <head> tag
$(document).ready(function () {
    $.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
        $("#hello").text(data.hello);
    });
}
);