#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const content = JSON.parse(body);
    for (let i = 0; content.results[i] !== undefined; i++) {
      if (content.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
