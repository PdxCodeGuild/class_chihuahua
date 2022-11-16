from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .models import register

def todo_item(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        description = request.POST['description']
        created_date = request.POST['created date']
        completed_date = request.POST['completed date']

        Todo.objects.create(description = description, created_date = created_date, completed_date = completed_date)

    context = {
        'todo': todo
    }
    return render(request, 'pages/todo_item.html', context)

def display_todo(request):
    if request.method == 'POST':
        post = display_todo()
        post.description = request.POST['description']
        post.created_date = request.POST['created date']
        post.completed_date = request.POST['completed date']
        post.save()
        return render(request, 'pages/display_todo.html')
    else:
        return render(request, 'pages/display_todo.html')