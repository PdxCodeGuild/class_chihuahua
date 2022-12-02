const btn1 = document.getElementById('btn')
const todoList = document.getElementById('todo')


// const textnode = document.createTextNode(testField)

btn1.addEventListener('click', function(){
    const testField = document.getElementById('text').value
    const liNode = document.createElement('LI')
    liNode.innerHTML=testField
    todoList.appendChild(liNode)
    // console.log('hello')  

})