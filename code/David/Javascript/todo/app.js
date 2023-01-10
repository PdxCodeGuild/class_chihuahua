const todoForm = document.getElementById('todo-form');
const todoInput = document.getElementById('todo-input');
const todoList = document.getElementById('todo-list');
const completedList = document.getElementById('completed-list');

todoForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const todoText = todoInput.value;
  todoInput.value = '';

  const todoItem = {
    text: todoText,
    completed: false,
  };

  const todoEl = document.createElement('li');
  todoEl.innerText = todoItem.text;
  todoList.appendChild(todoEl);

  const completeButton = document.createElement('button');
  completeButton.innerText = 'Complete';
  todoEl.appendChild(completeButton);

  completeButton.addEventListener('click', () => {
    todoItem.completed = true;
  
    // add a line through the completed to-do item
    todoEl.style.textDecoration = 'line-through';
  
    // remove the "Complete" button
    completeButton.remove();
  
    completedList.appendChild(todoEl);
  });
  
});
