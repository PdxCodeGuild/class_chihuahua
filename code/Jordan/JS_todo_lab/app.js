let completedList = document.querySelector('#completed')
let appendList = document.querySelector('#todo')
let addButton = document.querySelector('#task-submit');
addButton.addEventListener('click', function() { //when the user clicks the add button, it will run the function
    let userInput = document.querySelector('#new-task-input').value
    let newTodo = document.createElement('li') //creating an html list element

    let deleteButton = document.createElement('button') // creating a delete button
    deleteButton.classList.add('delete')
    deleteButton.innerText = 'Delete' // the content within the tags, only accepts strings

    let completeButton = document.createElement('button') // creating a complete button
    completeButton.classList.add('complete')
    completeButton.innerText = 'Complete'

    newTodo.innerHTML = `${userInput}`
    newTodo.appendChild(completeButton)
    newTodo.appendChild(deleteButton)

    appendList.appendChild(newTodo) 
    completeButton.addEventListener('click', function() {
        appendList.removeChild(newTodo)
        let deleteComplete = document.createElement('button')
        deleteComplete.classList.add('delete-complete')
        deleteComplete.innerText = 'Delete'

        let completedTodo = document.createElement('li')
        completedTodo.innerText = userInput
        completedTodo.appendChild(deleteComplete)
        completedList.appendChild(completedTodo)
        deleteComplete.addEventListener('click', function() {
            completedList.removeChild(completedTodo)
        })
    })
    deleteButton.addEventListener('click', function() {
        appendList.removeChild(newTodo)
    })
    

} )
