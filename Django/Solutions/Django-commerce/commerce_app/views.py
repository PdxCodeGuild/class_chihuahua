from django.shortcuts import render, redirect
from .models import Product, Cart

def add_product(request):
    if request.method == "GET":
        return render(request, 'create_product.html')
    elif request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        price = int(request.POST['price'])
        print(name, description, price)
        Product.objects.create(name=name, description=description, price=price)
        return redirect('add_product')


def all_products(request):
    all_products = Product.objects.all()
    return render(request, 'all_products.html', {"all_products": all_products})

def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    current_cart = Cart.objects.filter(user=request.user).first()
    product.cart = current_cart
    product.save()
    return redirect('all_products')

def cart(request):
    current_cart = Cart.objects.filter(user=request.user).first()
    products_in_cart = Product.objects.filter(cart=current_cart)
    total = 0
    for product in products_in_cart:
        total+=product.price
    print(products_in_cart, total)
    context = {
        "products_in_cart": products_in_cart,
        "total": total
    }
    return render(request, 'cart.html', context)