// Write a Javascript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:
// Cannot use document.querySelector() to select HTML tag
// Must use the JQUERY API
$('#red_header').click(function() {
  $('header').css('color', '#FF0000');
});