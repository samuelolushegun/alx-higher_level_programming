#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exot(1);
  }
  const films = JSON.parse(body).results;
  const moviesIn = films.filter(film =>
    film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
  );
  console.log(moviesIn.length);
});
