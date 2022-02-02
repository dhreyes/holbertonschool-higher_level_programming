#!/usr/bin/node
// Write a script that prints the number of movies where the character "Wedge Antilles" is present
// The first argument is the API URL of the star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character number 18 in the Star Wars films, script must use this ID for filtering result
// Must use the module request

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }
    const data = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < data.characters.length; i++) {
        if (data.characters[i].includes('18')) {
            count++;
        }
    }
    console.log(count);
});