#!/usr/bin/node
const axios = require('axios').default;

async function addUser (data) {
  try {
    const response = await axios.get('https://swapi-api.alx-tools.com/api/films/3/');
    const newArray = Object.values(response.data);

    const getCharacter = async (newArray) => {
      for (let i = 0; i < newArray[6].length; i++) {
        if (i === 6) {
          const arryPeople = newArray[i];
          for (let j = 0; j < arryPeople.length; j++) {
            const people = await axios.get(arryPeople[j]);
            const newPeople = Object.values(people.data);
            console.log(newPeople[0]);
          }
        }
      }
    };

    getCharacter(newArray);
  } catch (error) {
    console.error(error);
  }
}

addUser();
