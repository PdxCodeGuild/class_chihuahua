const todos = ["task 1", "task 2",]
let task = document.getElementById('todo_text')
let add = document.getElementById('add')
let list = document.getElementById('list')

add.addEventListener("click", function (event) {
    todos.push(task.value)
    console.log(todos)
});

for (let i = 0; i < todos.length; i++) {
    console.log(todos[i])
    let new_event = document.createElement('li');
    let complete_button = document.createElement("button");
    new_event.setAttribute("id", "todo_event")
    complete_button.addEventListener('click', function (event) {
        task = new_event;
        completed_area = document.getElementById("completed");
        completed_area.appendChild(task);
        console.log("works");
        complete_button.remove();
    });
    new_event.innerHTML = todos[i];
    complete_button.innerHTML = 'complete';
    list.appendChild(new_event);
    list.appendChild(complete_button);
    let delete_button = document.createElement("button");
    delete_button.addEventListener("click", function (event) {
        task = new_event
        delete_button.remove();
        delete todos[i];
        console.log(todos);
    });
    delete_button.innerHTML = "delete";
    list.appendChild(delete_button);
};