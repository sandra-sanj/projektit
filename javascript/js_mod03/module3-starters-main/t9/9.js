'use strict';

const formula = document.querySelector('#calculation');

const button = document.querySelector('#start');
button.addEventListener('click', (event) => {
    console.log(formula.value);
    
    let parts;
    let operation;
    for (let item of ['+', '-', '*', '/']) {
        if (formula.value.includes(item)) {
            operation = item;
            parts = formula.value.split(operation);
        }
    }
    console.log(parts);
    console.log(operation);
    
    
    const numbers = [];
    for (let item of parts) {
        numbers.push(parseFloat(item));
    }
    console.log(numbers);
    
    const result = calculate(numbers[0], numbers[1], operation);
    printResult(result);
    
});

function calculate(number1, number2, operation) {
    let result;
    if (operation === '+') {
        result = number1 + number2;
    } else if (operation === '-') {
        result = number1 - number2;
    } else if (operation === '*') {
        result = number1 * number2;
    } else if (operation === '/') {
        result = number1 / number2;
    }
    console.log(result);
    return result;
}

function printResult(text) {
    const element = document.querySelector('#result');
    element.textContent = text;
}
