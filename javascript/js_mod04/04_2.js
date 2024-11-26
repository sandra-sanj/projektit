'use strict';

async function getTVShow(input) {
    try {
        const response = await fetch('https://api.tvmaze.com/search/shows?q=' + input);
        
        if (!response.ok) {
            throw new Error(response.status.toString());
        }
        const result = await response.json();
        console.log('results:')
        console.log(result);
        for (const item of result) {
            console.log(item);
        }
        
    } catch (error) {
        console.error(error);
    }
}

const form = document.querySelector('#form')
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const input = form.querySelector('input').value;
    getTVShow(input);
});
