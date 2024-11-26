'use strict';

async function getRandomJoke(input) {
    // empty existing results element or create new if does not exist
    let divElem;
    const existingElem = document.querySelector('#results');
    if (existingElem) {
        existingElem.innerHTML = '';
        divElem = existingElem
    } else {
        divElem = document.createElement('div');
        divElem.id = 'results';
        document.body.appendChild(divElem);
    }
    
    try {
        const response = await fetch('https://api.chucknorris.io/jokes/search?query=' + input);
        if (!response) {
            throw new Error(response.status.toString());
        }
        const result = await response.json();
        console.log(result.result);
        
        for (const item of result.result) {
            const joke = item.value;
            console.log(joke);
            
            const articleElem = document.createElement('article');
            divElem.appendChild(articleElem);
            
            const p = document.createElement('p');
            p.textContent = joke;
            articleElem.appendChild(p);
        }
        
    } catch (error) {
        console.error(error);
    }
}

const form = document.querySelector('#form');
form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const input = form.querySelector('#query').value;
    getRandomJoke(input);
})
