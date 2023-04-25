#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const route = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(route, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
