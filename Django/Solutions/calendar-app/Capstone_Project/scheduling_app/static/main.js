console.log("hello from main.js");


let message = document.getElementsByClassName('alert')
console.log(message)
setTimeout(function(){ message[0].remove() }, 3000);