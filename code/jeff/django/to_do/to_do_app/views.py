from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def list_index(request):
    index_list = TodoItem.objects.all()  # gets all of the to do lists from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'index_list': index_list
    }
    return render(request, 'pages/index.html', context)

def new(request):
    if request.method == "GET":
        return render(request, 'pages/new.html')
    elif request.method == "POST":
        title = request.POST['title']
        print(title)
        title = request.POST['title']
        description = request.POST['description']
        created_date = request.POST['created_date']
        completed_date = request.POST['completed_date']
        completed = request.POST['completed_check']
        if completed == 'on': 
            completed = True
        TodoItem.objects.create(title=title, description=description, created_date=created_date, completed_date=completed_date, completed=completed)
        return redirect('new')


def edit(request, pk):
    todo = TodoItem.objects.get(id= pk)
    form = TodoItemForm(instance=todo)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    
    #return redirect('edit')
    return render(request, 'pages/edit.html', context)
    


