#!/usr/bin/node
const { error } = require('console')
const request = require('request')
filmsId  = process.argv[2]
url = `'https://swapi-api.alx-tools.com/api/films/${films}/`

request(url,(error, response, body) =>{
  if(error){
    console.error(error)
    return;
  }
  if(response.statusCode == 200){
    arrayPeople = JSON.parse(body.characters)
    console.log(arrayPeople);
    
  }
})


// #!/usr/bin/node
// const axios = require('axios').default;

// films = process.argv[2]

// async function addUser (data) {
//   try {
//     const response = await axios.get('https://swapi-api.alx-tools.com/api/films/${films}/');
//     const newArray = Object.values(response.data);

//     const getCharacter = async (newArray) => {
//       for (let i = 0; i < newArray[6].length; i++) {
//         if (i === 6) {
//           const arryPeople = newArray[i];
//           for (let j = 0; j < arryPeople.length; j++) {
//             const people = await axios.get(arryPeople[j]);
//             const newPeople = Object.values(people.data);
//             console.log(newPeople[0]);
//           }
//         }
//       }
//     };

//     getCharacter(newArray);
//   } catch (error) {
//     console.error(error);
//   }
// }

// addUser();
