#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function req (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}

async function print () {
  try {
    const body = await req(url);
    const characters = JSON.parse(body).characters;

    for (let i = 0; i < characters.length; i++) {
      const characterBody = await req(characters[i]);
      console.log(JSON.parse(characterBody).name);
    }
  } catch (error) {
    console.error(error);
  }
}

print();
