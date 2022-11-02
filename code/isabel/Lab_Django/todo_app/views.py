from django.shortcuts import render, redirect, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, 'home.html')

def data_collection(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        task = request.POST['task']
        # # start_date = request.POST['start_date']
        # # end_date = request.POST['end_date']
        # # completion = request.POST['completion']
        # print(task)
        # # print(task, start_date, end_date, completion)
        return HttpResponse('Thank you')
        