from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem


def home(request):
    return HttpResponse("Here is your to do list.")

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





def edit(request):
    if request.method == "GET":   
        return render(request, 'pages/edit.html')
    elif request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        created_date = request.POST['created_date']
        completed_date = request.POST['completed_date']
        completed = request.POST['completed_check']
        if delete == 'on': 
            delete = True,
        TodoItem.objects.delete(title=title, description=description, created_date=created_date, completed_date=completed_date, completed=completed)
        title = request.POST['title']

