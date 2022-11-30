const textField = document.getElementById("thing_todo");
const todo_item = document.getElementById("todo_item");
const trigger = document.getElementById("trigger");
let incompleteUl = document.getElementById("incomplete");

trigger.addEventListener("click", function() {
    // console.log(textField.value);
    // incompleteUl.appendChild(textField.value);
    incompleteUl.innerHTML = `<li>${textField.value}</li>`;

});