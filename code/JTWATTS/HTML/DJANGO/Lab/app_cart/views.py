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
    


def about(request):
    return render(request, 'choice.html')

def basket(request):
    fruit  = Produce.objects.all()
    print(fruit)
    return render(request, 'home.html', {"fruit": fruit})
def addtocart(request):
    if request.method == "POST":
        item = Produce.objects.create(
        title = request.POST['fruit'],
        fruit = request.POST['fruit'],
        cost = 1.00,
        )
        return HttpResponseRedirect(reverse('home'))






















































# Create your views here.
