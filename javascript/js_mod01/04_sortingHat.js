'use strict';

function sortingHat() {
    
    const name = prompt('Enter your name: ');
    
    const randomNumber = Math.random();
    const number = Math.floor(randomNumber * 4 + 1);
    console.log(number);
    
    let house;
    switch (number) {
        case 1:
            house = 'Gryffindor';
            break;
        case 2:
            house = 'Slytherin';
            break;
        case 3:
            house = 'Hufflepuff';
            break;
        case 4:
            house = 'Ravenclaw';
            break;
        default:
            house = 'unknown house';
    }
    
    const resultsPrint = `${name}, you are in ${house}.`;
    
    const element = document.querySelector('#text');
    element.innerHTML = resultsPrint;
}
