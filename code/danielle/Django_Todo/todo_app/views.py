from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def todo_item(request):
    if request.method=="POST":
        post=Todo()
        post.description=request.POST['description']
        post.created_date=request.POST['created_date']
        post.completed_todo=request.POST['completed_todo']
        post.save()
        return redirect('/display')
    return render(request, 'pages/todo_item.html')

def display_todo(request):
    all_todos = Todo.objects.all()
    return render(request, 'pages/display_todo.html', {'all_todos': all_todos})

def completed_list(request):
    if request.method=="POST":
        completed_todos = Todo.objects.filter(completed_todo = True)
        return redirect('/completed')
    return render(request, 'pages/completed_list.html', {'completed_todos': completed_todos})