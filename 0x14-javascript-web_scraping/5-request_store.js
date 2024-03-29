#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const route = process.argv[2];
const fileName = process.argv[3];

request(route, (err, res, body) => {
  if (err) throw err;

  fs.writeFile(fileName, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
