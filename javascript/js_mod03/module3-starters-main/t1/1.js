'use strict';

const element = document.querySelector('#target');

let resultsString = '';
for (const item of ['First item', 'Second item', 'Third item']) {
    resultsString += `<li>${item}</li>`;
}
element.innerHTML = resultsString;

element.classList.add('my-list');
console.log(element.classList.value);
