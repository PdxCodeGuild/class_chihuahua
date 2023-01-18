from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import item
from django.views.generic import View
from django import forms
from django.contrib.auth.forms import UserCreationForm
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here

def landing(request):
    return render(request, 'landing.html')
class RegisterForm(UserCreationForm):
    pass
def register(request):
    form = RegisterForm()
    return render(request, "register_page.html", {'form':form})

def login_page(request):
    return render(request, "login_page.html")

def profile(request):
    return render(request, "profile_page.html")


def fight(request):
    all_objects = item.objects.all()
    random_item_1 = random.choice(all_objects)
    random_item_2 = random.choice(all_objects)
    ai_attack = random_item_1.attack + random_item_2.attack
    ai_defense = random_item_1.defense + random_item_2.defense
    context = {
        "ai_attack": ai_attack,
        "ai_defense": ai_defense,
        "random_item_1": random_item_1,
        "random_item_2": random_item_2,
    }
    return render(request, 'fight_page.html', context)

class inventory(View):
    def get(self, request):
        items = item.objects.all
        template = loader.get_template("inventory.html")
        context = {
            "items": items,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        items = item.objects.all
        data = item.objects.all()
        template = loader.get_template("inventory.html")
        context = {
            "items": items,
            "data": data,
        }
        return HttpResponse(template.render(context, request))

@csrf_exempt
def move_data(request):
    if request.method == 'POST':
        data_models = request.POST.getlist('dataModels')
        for id in data_models:
            try:
                data_model = item.objects.get(id=id)
                context = {
                    "data_model" : data_model,
                }
                return redirect('fight_page', context)
            except item.DoesNotExist:
                return HttpResponse('Data model not found', status=404)
    else:
        return HttpResponse('Invalid request', status=405)