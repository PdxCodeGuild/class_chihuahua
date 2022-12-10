from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo_Item


def todo(request):
    if request.method == "GET":
        return render(request, 'todo/todo.html')
    elif request.method == 'POST': 
        title = request.POST['title'] 
        text = request.POST['text']  
        Todo_Item.objects.create(title = title, text = text)
        return redirect('list')

def todo_list(request):
    todo_items = Todo_Item.objects.all()
    context = { 'todo_items' : todo_items} 
    return render(request, 'todo/list.html',context)

def update(request, id):
    todo = Todo_Item.objects.get(id = id)
    return render(request, 'todo/update.html', {"todo": todo})

def delete(request, id):
    todo = Todo_Item.objects.get(id = id)
    todo.delete()
    return redirect('list')