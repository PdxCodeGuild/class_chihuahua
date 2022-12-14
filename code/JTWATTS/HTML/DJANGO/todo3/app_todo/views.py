from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.urls import reverse
from datetime import datetime

# def todo_list(request):
#     return HttpResponse(request, 'base.html')

def todo_list(request):
    todos = Todo.objects.all()

    context= {
        'todos': todos
       
    }
    return render(request, 'todos/todo_list.html', context)

def add_todo(request):
    if request.method == 'GET': # if its a GET request, just display the todos/add.html template
        return render(request, 'todos/add.html')
    elif request.method == 'POST': # if it's a POST request ...
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        if (request.POST['status'] == 'False'): # check the status because it's a string and booleans are not strings
            status = False
        else:
            status = True
        # add the new todo to the databse. objects.create() automatically saves the new todo for us so we
        # don't need a separate call to the save() method
        time_tocompletion=Todo.objects.create(title = title, text = text, status = status)
        return HttpResponseRedirect(reverse("list"))

def completion(request, id):
    
        todo_object= Todo.objects.get(id = id)
        todo_object.completion=datetime.now()# this takes the item and gives it a new time 
        todo_object.save()#saves to the backend
        return HttpResponseRedirect(reverse("list"))
 
def details(request, id):
    todo = Todo.objects.get(id = id)

    return render(request, 'todos/detail.html', {"todo": todo})


def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return HttpResponseRedirect(reverse("list"))

# view to remove a specific todo from the database specified by its id
def remove_todo(request, id):
    todo = Todo.objects.all().filter(id = id)
    todo.delete()
    return HttpResponseRedirect(reverse("list"))
# def update(request, date):
#     todo = Todo.objects.get(date = date)
#     if request.method == 'GET':
#         return render(request, 'todos/update.html', {'todo': todo})
#     elif request.method == 'POST':
#         todo.title = request.POST['title']
#         todo.text = request.POST['text']
#         if (request.POST['status'] == 'False'):
#             todo.status = False
#         else:
#             todo.status = True
#         todo.save()
#         return redirect('details', todo.date)      
# Create your views here.


# Create your views here.
