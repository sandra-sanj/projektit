'use strict';

function sqrt() {
    
    const calculate = confirm('Should I calculate the square root?');
    console.log(calculate);
    
    let resultsPrint;
    switch (calculate) {
        case true:
            const number = parseFloat(prompt('Enter number:'));
            
            const sqrt = Math.sqrt(number);
            console.log(sqrt);
            
            if (number < 0) {
                resultsPrint = `The square root of a negative number is not defined.`;
            } else {
                resultsPrint = `Square root of ${number} is ${sqrt}.`;
            }
            break;
        
        default:
            resultsPrint = `The square root is not calculated.`;
    }
    
    const element = document.querySelector('#text');
    element.innerHTML = resultsPrint;
}
