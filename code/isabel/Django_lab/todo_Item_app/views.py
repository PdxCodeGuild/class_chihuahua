from django.shortcuts import render, redirect
# from django.http import HttpResponse 
from .models import TodoItem



# Create your views here.
def home(request):
    return render(request, 'home.html')

def show_todo(request):
    todos = TodoItem.objects.all()

    context = {
        'todos': todos
    }

    return render(request, 'show_todo.html', context)

def add_todo(request):
    if request.method == 'GET':
        return render(request, 'add_todo.html')
    elif request.method == 'POST':
        title = request.POST['title']
        task = request.POST['task']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        completion = request.POST['completion']
        if (request.POST['completion'] == 'False'):
            completion = False
        else:
            completion = True
        # print(task, start_date, end_date, completion)
        TodoItem.objects.create(title=title, task=task, start_date=start_date, end_date=end_date, completion=completion)
        return redirect('show')

    
def update(request, id):
    todo = TodoItem.objects.get(id=id)
    if request.method == 'GET':
        context = {
            "todo": todo
        }
        return render(request, 'update.html', context)
    elif request.method == "POST":
        todo.title = request.POST['title']
        todo.task = request.POST['text']
        todo.start_date = request.POST['start_date']
        todo.end_date = request.POST['end_date']   
        if (request.POST['completion'] == 'FALSE'):
            todo.completion = False
        else:
            todo.completion = True 

        todo.save()
        return redirect('show_todo.html', todo.id)

def remove_todo(request, id):
    todo = TodoItem.objects.get(id=id)
    todo.delete()
    return redirect('show_todo.html')
