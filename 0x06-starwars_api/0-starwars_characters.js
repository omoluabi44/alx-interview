#!/usr/bin/node

const request = require('request');
const filmsId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmsId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const arrayPeople = JSON.parse(body);
    const allCharacters = arrayPeople.characters;

    allCharacters.forEach(element => {
      request(element, (ElementError, res, bdy) => {
        if (ElementError) {
          console.error(ElementError);
        }
        if (res.statusCode === 200) {
          const allPeople = JSON.parse(bdy);
          console.log(allPeople.name);
        }
      });
    });
  }
});
