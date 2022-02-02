#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  const results = data.results;
  console.log(data)
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    if (data.characters[i].includes('18')) {
      count++;
    }
  }
  console.log(count.length);
});
