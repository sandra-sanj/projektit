'use strict';

const firstIntElement = document.querySelector('#num1');
const secondIntElement = document.querySelector('#num2');
const calcTypeElement = document.querySelector('#operation');

let firstValue = firstIntElement.value;
let secondValue = secondIntElement.value;
let calcType = calcTypeElement.value;

function logMessage() {
    const message = `${firstValue}, ${secondValue}, ${calcType}`;
    console.log(message);
}


firstIntElement.addEventListener('change', (event) => {
    firstValue = firstIntElement.value;
    logMessage();
});

secondIntElement.addEventListener('change', (event) => {
    secondValue = secondIntElement.value;
    logMessage();
});

calcTypeElement.addEventListener('change', (event) => {
    calcType = calcTypeElement.value;
    logMessage();
});


// calc button press
const calcButton = document.querySelector('#start');
calcButton.addEventListener('click', (event) => {
    
    let result;
    if (!firstValue || !secondValue) {
        result = 'Unable. Enter both numbers first.';
    } else {
        const int1 = parseFloat(firstValue);
        const int2 = parseFloat(secondValue);
        
        if (calcType === 'add') {
            result = int1 + int2;
        } else if (calcType === 'sub') {
            result = int1 - int2;
        } else if (calcType === 'multi') {
            result = int1 * int2;
        } else if (calcType === 'div') {
            result = int1 / int2;
        }
    }
    
    console.log(result);
    const resultElement = document.querySelector('#result');
    resultElement.textContent = result;
    
});
