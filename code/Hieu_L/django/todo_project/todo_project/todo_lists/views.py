from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import todo_item

# Create your views here.
def list(request):
    return render(request, 'todo/list.html')

def todo(request):
    if request.method == "GET":
        return render(request, 'todo/todo.html')
    elif request.method == "POST":
        chore = request.POST['text']
        todo_item.objects.create(text='chore')
        return redirect('item')