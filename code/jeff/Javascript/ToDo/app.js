const field = document.getElementById("user_input");
const word = document.getElementById("word");
const remove = document.getElementById("remove");
const trigger = document.getElementById("trigger");
const list = document.getElementById("list");
const completed = document.getElementById("completed");



trigger.addEventListener("click", function(event) { 
    const li = document.createElement("li");
    li.innerHTML = field.value;
    li.addEventListener("click", function (event){     
    event.target.classList.add("strike");
    completed.appendChild(event.target);
})
    list.appendChild(li);
})




