function loadButtons() {
    
    const addButton1 = document.querySelector('#script1');
    addButton1.addEventListener('click', () => {
        logToConsole();
    });
    
    const addButton2 = document.querySelector('#script2');
    addButton2.addEventListener('click', () => {
        userPrompt();
    });
    
    const addButton3 = document.querySelector('#script3');
    addButton3.addEventListener('click', () => {
        numbersMath();
    });
    
    const addButton4 = document.querySelector('#script4');
    addButton4.addEventListener('click', () => {
        sortingHat();
    });
    
    const addButton5 = document.querySelector('#script5');
    addButton5.addEventListener('click', () => {
        leapYear();
    });
    
    const addButton6 = document.querySelector('#script6');
    addButton6.addEventListener('click', () => {
        sqrt();
    });
    
    const addButton7 = document.querySelector('#script7');
    addButton7.addEventListener('click', () => {
        dice();
    });
    
    const addButton8 = document.querySelector('#script8');
    addButton8.addEventListener('click', () => {
        leapYearsWithinTimePeriod();
    });
    
    const addButton9 = document.querySelector('#script9');
    addButton9.addEventListener('click', () => {
        primeNumberFunction();
    });
    
    const addButton10 = document.querySelector('#script10');
    addButton10.addEventListener('click', () => {
        diceSumProbability();
    });
}

loadButtons();