function addItem(){
    var li = document.createElement("li");  
    var input = document.getElementById("todo");
    li.innerHTML = input.value;
    li.classList.add("todo-item")
    input.value = "";

    document.getElementById("incomplete").appendChild(li);
}

let complete = document.querySelector('#todo-item');
let incomplete = document.querySelector('#incomplete');

function todo(){
    incomplete.addEventListener('click', todo, false);
    complete.classList.toggle('reveal');
    console.log(todo)
}

