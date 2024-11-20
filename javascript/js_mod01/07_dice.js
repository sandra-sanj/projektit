'use strict';

function rollDice(times) {
    let rolls = [];
    for (let i = 1; i <= times; i++) {
        rolls.push(Math.floor(Math.random() * 6 + 1));
    }
    return rolls;
}

function sumDiceRolls(rollsList) {
    let sum = 0;
    for (let j = 1; j <= rollsList.length; j++) {
        const rollValue = rollsList[j - 1];
        sum += rollValue;
    }
    return sum;
}


function dice() {
    const rollsNumber = parseFloat(prompt('Enter number of dice rolls:'));
    const rolls = rollDice(rollsNumber);
    const element = document.querySelector('#text');
    element.innerHTML = sumDiceRolls(rolls).toString();
}
