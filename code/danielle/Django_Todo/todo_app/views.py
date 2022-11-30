from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo
from django.urls import reverse

def create(request):
    if request.method=="POST":
        description=request.POST['description']
        created_date=request.POST['created_date']
        Todo.objects.create(description=description, created_date=created_date)
        return HttpResponseRedirect(reverse("todo:display_todo"))

def display_todo(request):
    completed_todos = Todo.objects.filter(completed_todo = True)
    incomplete_todos = Todo.objects.filter(completed_todo = False)
    context = {
        "completed_todos": completed_todos,
        "incomplete_todos": incomplete_todos
        }
    return render(request, 'pages/display_todo.html', context=context)

def completed_list(request):
    if request.method=="POST":
        return redirect('/completed')
    return render(request, 'pages/completed_list.html', {'completed_todos': completed_todos})