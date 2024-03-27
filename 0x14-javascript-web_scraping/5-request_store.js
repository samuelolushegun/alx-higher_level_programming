#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const content = JSON.stringify(body);
  const fs = require('fs');
  const filePath = process.argv[3];
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
