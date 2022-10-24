from django.shortcuts import render
from .models import Product

#--> Rest
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import ProductSerializer 
from rest_framework.response import Response
#-->

def home(request):
  return render(request, 'home.html')

def chart(request):
  return render(request, 'chart.html')

@api_view(['GET', 'POST'])
def product_list(request, format=None):
    """
    Get a list of products or create a product .
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



