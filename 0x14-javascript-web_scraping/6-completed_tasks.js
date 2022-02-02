#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the request module

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
