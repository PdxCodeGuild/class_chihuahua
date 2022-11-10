from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def shortener(request):
    return render(request, 'pages/url.html')

def accepted(request):
    return render(request, 'pages/url.html')

def shortened(request):
    pass