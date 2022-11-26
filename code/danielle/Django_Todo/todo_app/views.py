from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def todo_item(request):
    if request.method=="POST":
        post=Todo()
        post.description=request.POST['description']
        post.created_date=request.POST['created_date']
        post.completed_date = request.POST['completed_date']
        post.save()
        return redirect('/redirect')
    return render(request, 'pages/todo_item.html')

def display_todo(request):
    all_todos = Todo.objects.all()
    return render(request, 'pages/display_todo.html', {'all_todos': all_todos})

    