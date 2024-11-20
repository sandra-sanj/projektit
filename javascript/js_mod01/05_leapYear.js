'use strict';

function leapYear() {
    
    const year = prompt('Enter year:');
    
    let leapYear = false;
    if (year % 4 === 0) {
        leapYear = true;
        
        if (year % 100 === 0 && (year % 400 !== 0)) {
            leapYear = false;
        }
    }
    console.log(leapYear);
    
    let isLeapYearText;
    switch (leapYear) {
        case true:
            isLeapYearText = 'is';
            break;
        default:
            isLeapYearText = 'isn\'t';
    }
    console.log(isLeapYearText);
    
    const resultsPrint = `${year} ${isLeapYearText} a leap year.`;
    
    const element = document.querySelector('#text');
    element.innerHTML = resultsPrint;
}
