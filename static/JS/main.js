
// List of words displayed on banner
// with typing animation
const words = ['web development', 'front-end development', 'back-end development', 'dev-ops', 'web app security']
let count = 0
let index = 0
let currentText = ''
let letter = ''

console.log('run');

// OPEN AND CLOSING PARENTHESIS AROUND FUNCTION
// TO AUTOMATICALLY CALL IT AND () @ END TO INVOKE
(function typing() {

    if(count === words.length){
        count = 0;
    }
    currentText = words[count];
   
    letter = currentText.slice(0,++index)

    document.querySelector('.typing').textContent = letter;
    if (letter.length === currentText.length) {
        count++
        index = 0
    }

    setTimeout(typing, 300)
    
})()