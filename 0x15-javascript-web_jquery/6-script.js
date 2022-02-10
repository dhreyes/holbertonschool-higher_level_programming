// Write a Javascript script that updates the text of the <header> element to New Header!!! when the user clicks on the tag DIV#update_header:
// Cannot use document.querySelector() to select HTML tag
// Must use the JQUERY API
$('#update_header').click(function() {
    $('header').text('New Header!!!');
    }
);