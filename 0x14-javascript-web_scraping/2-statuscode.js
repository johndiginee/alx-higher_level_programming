#!/usr/bin/node
const request = require('request');
const route = process.argv[2];

request(route, (err, res, body) => {
  if (!err) console.log('code:', res.statusCode);
});
