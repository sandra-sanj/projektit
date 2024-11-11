function printInHTML(result) {
    const element = document.querySelector('#text');
    element.innerHTML = result;
}

function diceSumProbability() {
    
    const diceCount = parseInt(prompt('Enter the number of dice:'));
    const interestingEyeSum = parseInt(prompt('Enter interesting eye sum:'));
    console.log(`${diceCount} dice, ${interestingEyeSum} sum`);
    
    if (diceCount < 1 || isNaN(diceCount) || isNaN(interestingEyeSum)) {
        return printInHTML('No dice rolled');
    }
    
    const simulationsCount = 10000;
    
    let allRolls = [];
    for (let i = 1; i <= simulationsCount; i++) {
        const diceRolls = rollDice(diceCount);
        allRolls.push(diceRolls);
    }
    
    let diceRollSums = [];
    for (let i = 0; i < allRolls.length; i++) {
        diceRollSums.push(sumDiceRolls(allRolls[i]));
    }
    
    const counter = {};
    diceRollSums.forEach(element => {
        if (counter[element]) {
            counter[element]++;
        } else {
            counter[element] = 1;
        }
    });
    console.log(counter);
    
    let probability = 0; // failsafe
    if (interestingEyeSum in counter) {
        const favorableEventCount = counter[interestingEyeSum];
        console.log(favorableEventCount);
        probability = ((favorableEventCount / simulationsCount) * 100).toFixed(2);
    }
    
    const result = `Probability to get sum ${interestingEyeSum} with ${diceCount} dice is ${probability}%`;
    return printInHTML(result);
}
