'use strict';

document.addEventListener('mouseover', (event) => {
    const thing = event.relatedTarget;
    console.log(thing);
    
    const imageElement = document.querySelector('#target');
    
    console.log(thing.id);
    if (thing.id === 'trigger') {
        console.log('ok');
        imageElement.src = 'img/picB.jpg';
    } else {
        imageElement.src = 'img/picA.jpg';
    }
});
