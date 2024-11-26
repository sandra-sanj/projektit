'use strict';

async function getTVShow(input) {
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
        const response = await fetch('https://api.tvmaze.com/search/shows?q=' + input);
        
        if (!response.ok) {
            throw new Error(response.status.toString());
        }
        const result = await response.json();
        console.log('results:')
        console.log(result);
        
        for (const item of result) {
            console.log(item.show)
            const name = item.show.name;
            const link = item.show.url;
            const medImg = item.show.image ? item.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
            const summary = item.show.summary;
            
            const articleElem = document.createElement('article');
            divElem.appendChild(articleElem);
            
            const h2 = document.createElement('h2');
            h2.textContent = name;
            articleElem.appendChild(h2);
            
            const urlElem = document.createElement('a');
            urlElem.textContent = link;
            urlElem.target = '_blank';
            articleElem.appendChild(urlElem);
            
            const imgElem = document.createElement('img');
            imgElem.src = medImg;
            imgElem.alt = name;
            articleElem.appendChild(imgElem);
            
            const summaryElem = document.createElement('div');
            summaryElem.textContent = summary;
            articleElem.appendChild(summaryElem);
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
