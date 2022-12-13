from django.shortcuts import render, redirect
from .models import Blog

def home(request):
    return render(request, 'home.html')

def add_blog(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == "POST":
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        Blog.objects.create(title=title, text=text, pub_date=pub_date)
        return redirect('list')

def blog_list(request):
    blog_posts = Blog.objects.all()   
    return render(request, 'list.html', {"blog_posts": blog_posts})


def delete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    print(blog_post)
    blog_post.delete()
    return redirect('list')

def post_details(request, id):
    blog_post = Blog.objects.get(id=id)
    return render(request, 'details.html', {"blog_post": blog_post})

def update_post(request, id):
    blog_post = Blog.objects.get(id=id)
    blog_post.title = request.POST['title']
    blog_post.text = request.POST['text']
    blog_post.pub_date = request.POST['pub_date']
    print(blog_post)
    blog_post.save()
    return redirect('list')


def search_post(request):
    search = request.POST['search_blog']
    blog_posts = Blog.objects.filter(title__startswith=search)
    return render(request, 'home.html', {"blog_posts":blog_posts})
