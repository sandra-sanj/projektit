'use strict';

const element = document.querySelector('#target');

for (const item of ['First item', 'Second item', 'Third item']) {
    const newElement = document.createElement('li');
    newElement.textContent = item;
    element.appendChild(newElement);
}

element.classList.add('my-item');
