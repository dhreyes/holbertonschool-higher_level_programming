#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file
// The first argument is the URL to request
// The second argument is the file path to store the body response
// File must be UTF-8 encoded
// You must use the request module

const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
        if (err) {
        console.error(err);
        return;
        }
    });
    });