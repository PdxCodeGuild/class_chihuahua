const textField = document.getElementById("thing_todo");
const todo_item = document.getElementById("todo_item");
const trigger = document.getElementById("trigger");
let incompleteUl = document.getElementById("incomplete");
let incompleteList = document.getElementsByClassName("list_incomplete")
const body = document.querySelector('body')

trigger.addEventListener("click", function(event) {
    // add event listener to button id,
    // create element
    // add text from input to that new element
    // append this new element with new text as child
    // clear input box by targeting input box id set value to empty ""
    let itemList = document.createElement("li");
    itemList.innerHTML = textField.value;
    incompleteUl.appendChild(itemList);   
    document.getElementById("thing_todo").value = '';
});

// incompleteList.addEventListener("click", function(event) {
//     for (let i = 0; i < incompleteList.length; i++) {
//         let item = incompleteUl.children[i];
//         if (event.target.incompleteList.children[i] === true);
//         incompleteUl.removeChild(item)
//     }
// });

body.addEventListener('click', function(event) {
    if (event.target.tagName == 'LI') {
        event.target.remove('LI')
        let completedItem
        event.target.append
    }
})


