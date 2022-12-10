from django.shortcuts import render, redirect
import requests
from .models import Drink
from django.contrib import messages

def all_drinks(request):
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = response.json()
    drinks = data['drinks']
    for drink in drinks:
        Drink.objects.get_or_create(name=drink['strDrink'] , description=drink['strInstructions'], thumbnail=drink['strDrinkThumb'])
    all_drinks = Drink.objects.all()
    return render(request, 'viewall.html',{'all_drinks':all_drinks})

def fav_drinks(request):
    favs= Drink.objects.filter(favourite=True)
    return render(request, 'favs.html', {'favs': favs})

def mark_as_fav(request, id):
    print("THIS IS THE ID", id)
    drink = Drink.objects.get(id=id)
    if drink.favourite == False:
        drink.favourite = True
        messages.success(request, "Marked as fav!")
    else:
        drink.favourite = False
    drink.save()
    return redirect('all')