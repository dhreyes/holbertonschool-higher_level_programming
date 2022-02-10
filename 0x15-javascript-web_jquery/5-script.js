// Write a Javascript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
// Cannot use document.querySelector() to select HTML tag
// Must use the JQUERY API
$('#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
    }
);