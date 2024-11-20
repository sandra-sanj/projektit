'use strict';

function numbersMath() {
    
    const int1 = parseFloat(prompt('Input first number: '));
    const int2 = parseFloat(prompt('Input second number: '));
    const int3 = parseFloat(prompt('Input third number: '));
    
    const sum = int1 + int2 + int3;
    console.log(sum);
    
    const product = int1 * int2 * int3;
    console.log(product);
    
    const average = sum / 3;
    console.log(average);
    
    const resultsPrint = `Sum: ${sum}. Product: ${product}. Average: ${average}.`;
    
    const element = document.querySelector('#text');
    element.innerHTML = resultsPrint;
}
