// let todoItems = []; 

// function addTodo(text)
let addButton = document.querySelector('#task-submit');
addButton.addEventListener('click', function() { //when the user clicks the add button, it will run the function
    let userInput = document.querySelector('#new-task-input').value
    let appendList = document.querySelector('#todo')

    let newTodo = document.createElement('li') //creating an html list element
    newTodo.innerHTML = `${userInput}
    <button class="complete">Complete</button> 
    <button class="remove">Remove</button>` //on the inside of the li, insert this stuff
    appendList.appendChild(newTodo) //creating an object so we can access them later

    // let removeButton = document.querySelectorAll('.remove');
    // for(i in removeButton) {
    //     removeButton[i].addEventListener('click', function() {
    //     }) 
    // }
    let completeButton = document.querySelectorAll('.complete');
    for(i in completeButton) {
        completeButton[i].addEventListener('click', function(){
            console.log(appendList[0])
        })
    }
} )
