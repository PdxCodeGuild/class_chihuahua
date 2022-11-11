from django.shortcuts import render
import random, string
from .models import *
from django.http import HttpResponseRedirect #instead of rendering a page it runs a function
from django.urls import reverse #allow us to render a view instead


def home(request):
    url_objects = Url.objects.all()
    context = {
        "url_list": url_objects
    }
    return render(request, 'pages/home.html', context)

# def create(request):
#     url = request.POST['url']
#     return render(request, 'pages/url.html')

def random_(request): #refer to random password generator lab
    if request.method == 'POST':
        user_url = request.POST["users_url"]
        asce = string.ascii_letters
        new_url = ''.join(random.choice(asce) for i in range (6))
        create_url = Url.objects.create(
            long_url=user_url,
            short_url=new_url
        )
        return HttpResponseRedirect(reverse('home'))
    #taking the random choice of the asce letters and doing it 6 times, 
    # then the .join is taking the characters 


# def display():
#   urls = URLShortener.objects.all()
#   return render(request, 'blah.html, urls:url)
# for urls in url, it will build your link
# object.create is whenever I want to create an object in the back end(administrator)