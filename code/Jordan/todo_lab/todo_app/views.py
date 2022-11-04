from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime

def blog_posts(request):
    blogs = Blog.objects.all()  # gets all of the blog posts from the database and store them in a variable
  
    # creates the context dictionary to send the blog posts to the template
    context = {
       'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)

def add_post(request):
    if request.method == 'GET': # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST': # if it's a POST request ..
        title = request.POST['title']   # get the title from the POST submission, this comes from a form
        text = request.POST['text']     # get the text from the POST submission, this comes from a form
        #pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us.
        Blog.objects.create(title = title, text = text) #pub_date = pub_date
        return redirect('posts')
   
def delete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    print(blog_post) ## check the terminal, it should output the object before it gets deleted
    blog_post.delete()
    return redirect('posts')
    
def home(request):
    if request.method == 'GET':
        return render(request, 'pages/home.html')

def see_details(request, id): #we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Blog.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/details.html', {"post": post}) ## we are passing the context to the page

def complete_post(request, id):
    blog_post = Blog.objects.get(id=id)
    blog_post.completed_task = not blog_post.completed_task # the word not means the opposite of whatever comes next, so in this instance, we're flipping it to true
    blog_post.completed_date = datetime.now()
    print(blog_post)
    blog_post.save()
    return redirect('posts')

def edit_post(request, id):
    blog_post = Blog.objects.get(id=id)
    blog_post.title = request.POST['title']
    blog_post.text = request.POST['text']
    blog_post.save()
    return redirect('posts')