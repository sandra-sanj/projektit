'use strict';

function leapYearsWithinTimePeriod() {
    
    const startYear = parseInt(prompt('Enter start year:'));
    const endYear = parseInt(prompt('Enter end year:'));
    
    let year = startYear;
    let leapYears = [];
    
    do {
        let leapYear = false;
        if (year % 4 === 0) {
            leapYear = true;
            if (year % 100 === 0 && (year % 400 !== 0)) {
                leapYear = false;
            }
        }
        
        if (leapYear) {
            leapYears.push(year);
        }
        
        year += 1;
    } while (year <= endYear);
    console.log(leapYears);
    
    let newList = `<ul>${leapYears.map(leapYears => `<li>${leapYears}</li>`).join('')}</ul>`;
    const element = document.querySelector('#text');
    element.innerHTML = newList;
}
