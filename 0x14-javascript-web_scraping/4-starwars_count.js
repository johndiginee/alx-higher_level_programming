#!/usr/bin/node
const request = require('request');
const route = process.argv[2];
let count = 0;

request(route, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).results.forEach(result => {
    result.characters.forEach(character => {
      if (character.endsWith('18/')) count++;
    });
  });
  console.log(count);
});
