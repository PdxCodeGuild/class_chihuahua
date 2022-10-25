from django.shortcuts import render,redirect
from .models import Drink
import requests

def home(request):
    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a")
    data = response.json()
    for drink in data['drinks']:
        try:
            Drink.objects.create(drink_name = drink['strDrink'], drink_url = drink['strDrinkThumb'])
        except:
            continue
    all_drinks = Drink.objects.all()
    return render(request, 'home.html',{"all_drinks": all_drinks})

def mark_as_fav(request, id):
    drink = Drink.objects.get(id=id)
    if drink.favourite == True:
        drink.favourite = False
    else:
        drink.favourite = True
    drink.save()
    print("THIS IS MY DRINK", drink)
    return redirect('home')

def fav_list(request):
    fav_drinks = Drink.objects.filter(favourite = True)
    return render(request, 'list.html', {"fav_drinks": fav_drinks})
