function userPrompt() {
    
    const name = prompt('Input name: ');
    
    const element = document.querySelector('#text');
    const greeting = ('Hello, ' + name + '!');
    element.innerHTML = greeting;
}
