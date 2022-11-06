from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'todo/todo.html')

def list(request):
    return render(request, 'todo/list.html')
