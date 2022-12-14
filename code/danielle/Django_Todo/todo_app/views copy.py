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
    todos = Todo()
    form = request.POST
    completed_todos = Todo.objects.filter(completed_todo = True)
    incomplete_todos = Todo.objects.filter(incomplete_todo = False)
    context = {
        "completed_todos": completed_todos,
        "incomplete_todos": incomplete_todos
        }
    print(request.POST['complete'], "testing form")
    if form['complete'] == "on": #targeting form with value of complete (on/off should be value) Gotta remember boolean values
        todos.completed_todo == True
        todos.save()
    return render(request, 'pages/display_todo.html', context=context)

def completed_list(request):
    if request.method=="POST":
        completed_todo=request.POST['completed_todo']
        Todo.objects.filter(incompleted_todo=completed_todo)
        return HttpResponseRedirect(reverse("todo:display_todo"))