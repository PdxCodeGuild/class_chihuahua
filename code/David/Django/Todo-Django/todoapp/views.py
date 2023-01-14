from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    
    return render(request, 'todo_detail.html', {'todo': todo})