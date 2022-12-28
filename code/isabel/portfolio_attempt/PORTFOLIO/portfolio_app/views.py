from django.shortcuts import render

# Create your views here.
def portfolio_home(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    pass

def resume(request):
    pass