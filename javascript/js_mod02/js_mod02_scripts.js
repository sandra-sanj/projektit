'use strict';

function emptyElement(element) {
    while (element.firstElementChild) {
        element.firstElementChild.remove();
    }
}

// methods to insert text into html
function printListHTML(array, ordered = false, unordered = false) {
    let elementType;
    if (ordered) {
        elementType = 'ol';
    } else if (unordered) {
        elementType = 'ul';
    } else {
        return console.log('List element type not specified. Exited.');
    }
    
    const parentElement = document.querySelector('#result');
    emptyElement(parentElement);
    
    const newList = document.createElement(elementType);
    for (const item of array) {
        const newLi = document.createElement('li');
        newLi.textContent = item;
        newList.append(newLi);
    }
    parentElement.appendChild(newList);
}

function printInHTML(result, deletePrevious = true) {
    const parentElement = document.querySelector('#result');
    
    if (deletePrevious) {
        emptyElement(parentElement);
    }
    
    const newP = document.createElement('p');
    newP.textContent = result;
    parentElement.appendChild(newP);
}


// all buttons
function loadButtons() {
    
    const addButton1 = document.querySelector('#script1');
    addButton1.addEventListener('click', () => {
        printNumbersInReverse();
    });
    
    const addButton2 = document.querySelector('#script2');
    addButton2.addEventListener('click', () => {
        getParticipants();
    });
    
    const addButton3 = document.querySelector('#script3');
    addButton3.addEventListener('click', () => {
        getSixDogNames();
    });
    
    const addButton4 = document.querySelector('#script4');
    addButton4.addEventListener('click', () => {
        getInputUntilZero();
    });
    
    const addButton5 = document.querySelector('#script5');
    addButton5.addEventListener('click', () => {
        getUniqueInput();
    });
    
    const addButton6 = document.querySelector('#script6');
    addButton6.addEventListener('click', () => {
        rollDiceUntil6();
    });
    
    const addButton7 = document.querySelector('#script7');
    addButton7.addEventListener('click', () => {
        rollCustomDice();
    });
    
    const addButton8 = document.querySelector('#script8');
    addButton8.addEventListener('click', () => {
        runConcatString();
    });
    
    const addButton9 = document.querySelector('#script9');
    addButton9.addEventListener('click', () => {
        runEven();
    });
    
    const addButton10 = document.querySelector('#script10');
    addButton10.addEventListener('click', () => {
        voting();
    });
}

loadButtons();

// 1
function printNumbersInReverse() {
    const numbers = [];
    
    for (let i = 1; i <= 5; i++) {
        const number = parseInt(prompt('Enter number'));
        numbers.push(number)
    }
    console.log(numbers);
    
    for (let i = numbers.length - 1; i >= 0; i--) {
        console.log(numbers[i]);
    }
}

// 2
function getParticipants() {
    const participantCount = parseInt(prompt('Enter number of participants'));
    
    const names = [];
    for (let i = 1; i <= participantCount; i++) {
        const name = prompt('Enter name:');
        names.push(name);
    }
    console.log(names);
    
    names.sort();
    console.log(names);
    
    printListHTML(names, true, false);
}

// 3
function getSixDogNames() {
    const dogNames = [];
    
    for (let i = 1; i <= 6; i++) {
        const dogName = prompt(`Enter dog name ${i}:`);
        dogNames.push(dogName);
    }
    console.log(dogNames);
    printListHTML(dogNames, false, true);
}

// 4
function getInputUntilZero() {
    const numbers = [];
    let newNumber;
    do {
        newNumber = parseInt(prompt('Enter number:'));
        if (!isNaN(newNumber)) {
            numbers.push(newNumber);
        }
    } while (newNumber !== 0);
    console.log(numbers);
    
    numbers.sort((a, b) => b - a);
    console.log(numbers);
}

// 5
function getUniqueInput() {
    const numbers = [];
    let continueLoop = true;
    
    do {
        console.log(numbers);
        const newNumber = parseInt(prompt('Enter number:'));
        if (numbers.includes(newNumber)) {
            console.log('Number already in array!')
            continueLoop = false;
        } else if (!isNaN(newNumber)) {
            numbers.push(newNumber);
        }
    } while (continueLoop);
    
    numbers.sort((a, b) => a - b);
    console.log(numbers);
}

// 6, 7
function rollDice(sides) {
    return Math.floor(Math.random() * sides + 1);
}

// 6
function rollDiceUntil6() {
    const allDiceRolls = [];
    let diceRoll = 0;
    while (diceRoll !== 6) {
        diceRoll = rollDice(6);
        allDiceRolls.push(diceRoll);
    }
    console.log(allDiceRolls);
    printListHTML(allDiceRolls, false, true);
}

// 7
function rollCustomDice() {
    const diceSides = parseInt(prompt('Enter number of sides on dice:'));
    
    const allDiceRolls = [];
    let diceRoll = 0;
    while (diceRoll !== diceSides) {
        diceRoll = rollDice(diceSides);
        allDiceRolls.push(diceRoll);
    }
    console.log(allDiceRolls);
    printListHTML(allDiceRolls, false, true);
}

// 8
function concat(strings) {
    let concatString = '';
    for (const item of strings) {
        concatString += item;
    }
    return concatString;
}

// 8
function runConcatString() {
    const strings = ['Johnny', 'DeeDee', 'Joey', 'Marky'];
    console.log(strings);
    const result = concat(strings);
    console.log(result);
    printInHTML(result);
}

// 9
function runEven() {
    const numbers = [2, 7, 4, 3, 7, 8, 2];
    console.log(numbers);
    
    const evenNumbers = even(numbers);
    console.log(evenNumbers);
    
    function even(numbers) {
        const evenNumbers = [];
        for (const number of numbers) {
            if (number % 2 === 0) {
                evenNumbers.push(number);
            }
        }
        return evenNumbers;
    }
    printInHTML(`all: ${numbers}. even: ${evenNumbers}`);
}

// 10
function voting() {
    const candidateNumber = parseInt(prompt('Enter number of candidates:'));
    const candidateInfos = [];
    
    for (let i = 0; i < candidateNumber; i++) {
        const candidateName = prompt(`Name for candidate ${i + 1}`);
        candidateInfos.push({name: candidateName, votes: 0});
    }
    console.log(candidateInfos);
    
    // voting
    const voters = parseInt(prompt('Enter number of voters:'));
    for (let i = 0; i < voters; i++) {
        const votedCandidateName = prompt(`Enter candidate name to vote:`);
        
        for (const candidate of candidateInfos) {
            if (candidate.name === votedCandidateName) {
                candidate.votes += 1;
            }
        }
    }
    console.log(candidateInfos);
    
    // get winner
    candidateInfos.sort((a, b) => {
        const aVotes = a.votes;
        const bVotes = b.votes;
        console.log(aVotes, bVotes);
        return bVotes - aVotes;
    });
    console.log(candidateInfos);
    
    // print results
    printInHTML(`The winner is ${candidateInfos[0].name} with ${candidateInfos[0].votes} votes!`, false);
    printInHTML(`Results:`, false);
    for (const item of candidateInfos) {
        printInHTML(`${item.name}: ${item.votes} votes`, false);
    }
}
