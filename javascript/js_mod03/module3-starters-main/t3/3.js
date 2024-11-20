'use strict';
const names = ['John', 'Paul', 'Jones'];

const element = document.querySelector('#target');

let resultsString = '';
for (const item of names) {
    resultsString += `<li>${item}</li>`;
}
element.innerHTML = resultsString;
