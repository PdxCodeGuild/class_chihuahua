from django.shortcuts import redirect, render
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    fruit = Produce.objects.all()

    context = {
    "fruit" : fruit

    }

    return render(request, 'home.html',context)
    
def add_fruit(request):
    item = Produce.objects.get(id=id)
    count = Produce.objects.get(id=request.POST['fruit-select'])


def about(request):
    return render(request, 'choice.html')

def basket(request):
    fruit  = Produce.objects.all()
    print(fruit)
    return render(request, {"fruit": fruit},'home.html' )
def addtocart(request):
    if request.method == "POST":
        item = Produce.objects.create(
        title = request.POST['fruit'],
        fruit = request.POST['fruit'],
        cost = 1.00,
        )
        return HttpResponseRedirect(reverse('home'))


# def addtocart(request):
#     if request.method == "POST":
#         return render(request, "home/addtocart")
#         item = Produce.objects.create(
#         title = request.POST['fruit'],
#         fruit = request.POST['fruit'],
#         cost = 1.00
#     )
#     return HttpResponseRedirect(reverse('home'))





















































# Create your views here.
