// Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header:
// Cannot use document.querySelector() to select HTML tag
// Must use the JQUERY API
$('#red_header').click(function() {
    $('header').addClass('red');
    }
);