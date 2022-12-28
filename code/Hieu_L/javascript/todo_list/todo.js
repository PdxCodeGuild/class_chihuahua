let task = document.getElementById('todo_text')
let add = document.getElementById('add')
let list = document.getElementById('list')

add.addEventListener("click", function (event) {
    let new_event = document.createElement('li');
    let complete_button = document.createElement("button");
    new_event.innerHTML = task.value;
    new_event.setAttribute("id","todo_event")
    complete_button.setAttribute("id","complete_button");
    complete_button.innerHTML = 'complete';
    list.appendChild(new_event);
    list.appendChild(complete_button);
});

let complete = getElementById("complete_button")
// let completed = getElementById('completed')

complete_button.addEventListener('click', function (event) {
    console.log("works")
    // let todo_event = document.createElement('li');
    // let task = document.getElementsByTagName('todo_event')
    // todo_event.innerHTML = task.value;
    // completed.appendChild(li);
});
