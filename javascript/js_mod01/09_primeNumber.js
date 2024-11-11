function primeNumberFunction() {
    
    function primeNumber(number) {
        let isPrimeNumber = true;
        if (number <= 1) {
            isPrimeNumber = false;
        }
        
        for (let i = 2; i <= number - 1; i++) {
            if (number % i === 0) {
                isPrimeNumber = false;
            }
        }
        return isPrimeNumber;
    }
    
    const number = parseInt(prompt('Enter number:'));
    console.log(number);
    const isPrimeNumber = primeNumber(number);
    console.log(isPrimeNumber);
    
    const resultsPrint = `Is ${number} prime number? ${isPrimeNumber}`;
    const element = document.querySelector('#text');
    element.innerHTML = resultsPrint;
}
