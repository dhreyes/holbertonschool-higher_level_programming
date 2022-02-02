#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const users = {};
  for (const task of data) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  for (const user in users) {
    console.log(`${user}: ${users[user]}`);
  }
});
