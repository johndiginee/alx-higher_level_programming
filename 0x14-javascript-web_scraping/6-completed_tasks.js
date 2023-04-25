#!/usr/bin/node
const request = require('request');
const route = process.argv[2];
const numTasks = {};

request(route, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).forEach(todo => {
    const id = todo.userId;
    if (!numTasks[id]) numTasks[id] = 0;
    if (todo.completed) numTasks[id]++;
    if (numTasks[id] === 0) delete numTasks[id];
  });
  console.log(numTasks);
});
