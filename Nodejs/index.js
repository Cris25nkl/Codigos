const axios = require('axios');
const path = require('path');
const fs = require('fs').promises;


const main = async () => {
    let response = await axios.get('https://rickandmortyapi.com/api/character')
    let {data : {results}} =response;

    let character = results.map ((character) =>{
        return {
            id: character.id,
            name: character.name,
            status: character.status,
            species: character.species
        };
    }).map ((personaje)=>Object.values(personaje).join(',')).join('\n')
    await fs.writeFile(path.join(__dirname,'data.csv'), character)
    //console.log(path.join(__dirname,'data.csv'));
    //console.log(character);
}

main();