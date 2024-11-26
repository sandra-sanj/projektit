'use strict';

async function getRandomJoke() {
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/random');
        if (!response) {
            throw new Error(response.status.toString());
        }
        const result = await response.json();
        console.log(result.value);
        
    } catch (error) {
        console.error(error);
    }
}
getRandomJoke();
