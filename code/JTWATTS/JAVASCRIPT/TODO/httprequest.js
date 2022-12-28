// chapter 11
// javascript by default is non-blocking
//console.log('a') makes an http to a server
//console.log('b') loads elements on a page

function greeting(name){
    alert('hello ' + name)
}

function processUserInput(callback){
    const name = prompt('tell me your name ')

    
}

processUserInput(greeting)