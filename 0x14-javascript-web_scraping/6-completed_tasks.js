#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  }
  const complete = {};
  const todos = JSON.parse(body);
  for (const task of todos) {
    if (task.completed === true) {
      if (task.userId in complete) {
        complete[task.userId] += 1;
      } else {
        complete[task.userId] = 1;
      }
    }
  }
  console.log(complete);
});
