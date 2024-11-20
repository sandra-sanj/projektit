'use strict';

const form = document.querySelector('#source');
const firstName = document.querySelector('#source input[name="firstname"]');
const lastName = document.querySelector('#source input[name="lastname"]');
console.log(firstName, lastName);

const paragraph = document.querySelector('#target');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    console.log(firstName.value, lastName.value);
    paragraph.textContent = `Your name is ${firstName.value} ${lastName.value}`;
});
