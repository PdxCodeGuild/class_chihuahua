let task = document.getElementById('todo_text')
let add = document.getElementById('add')
let list = document.getElementById('list')

add.addEventListener("click", function (event) {
    let li = document.createElement('li');
    li.innerHTML = task.value;
    list.appendChild(li);
});