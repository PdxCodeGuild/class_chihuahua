from django.shortcuts import render, redirect
from . models import Short
from django.utils.crypto import get_random_string
from django.contrib import messages

# Create your views here.
def enter_url(request):
    if request.method == "GET":
        return render(request, 'enter_url.html')
    elif request.method == "POST":
        # creates dictionary
        url_entered = request.POST['url_entered']
        for u in url_entered:
            if 'https://' in url_entered:
                messages.warning(request, 'Remove HTTPS:// from the URL')
                return render(request, 'enter_url.html')
            else:
                decode_url = url_entered.split('/')
                random = get_random_string(length=5)
                ending_url = decode_url[0] + u + '/' + random
                shortened =  Short.objects.create(url = url_entered, code = ending_url)
                return render(request, 'show.html')
        


def show_all(request):
    url_list = Short.objects.all()
    context = {
        'url_list': url_list
    }
    if request.method == 'GET':
        return render(request, 'show.html', context)

# name="url" in template html in input refers to the key in veiws.py ['url']
# where the vars does not have to be the same name as the key in veiws.py
# the {% url 'add_url' %} refers to the urls.py name=