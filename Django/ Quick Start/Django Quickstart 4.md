## Create a reverse view

Let's create a view that displays a specific blog post. This view requires you to add a `<int:id>` in the URL. First of all, in the _my_app > urls.py page add:

```python
    path('details/<int:id>', views.see_details, name = 'see_details')
```

The entire page should now look like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts'),
    path('details/<int:id>', views.see_details, name = 'see_details')
]
```

- Inside _my_app > views.py add a view to return a page based on the ID of the element we are targeting:

```python
def see_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Blog.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/details.html', {"post": post}) ## we are passing the context to the page
```

- Update the Templates > Pages > Posts.html to look like the following:

```html
{% extends 'base.html' %}
{% block content %}
<a href="{%url 'add_posts' %}">add a blog post</a>
<ul>
  {% for post in blogs %}
  <p><a href="{%url 'details' post.id %}">Title: {{ post.title }}</a></p>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
  {% endfor %}
</ul>
{% endblock %}

```

As you can see we added an <a> tag with a link to page that is served by the view that we just added.

- As a last element, we need to add a page that displays the blog post by itself. In the Pages folder, add a `details.html` page:

```html
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'posts' %}">Back to main view</a></p>
<ul>
  <p>ID: {{ post.id }}</p>
  <p>Description: {{ post.text }}</p>
  <p>Pub Date: {{post.pub_date}}</p>
</ul>
{% endblock %}
```

## Update a blog post

Let's convert the `details.html`page into a form. Leave the form action attribute blank for the moment.

```html
{% extends 'base.html' %}
{% block content %}
<p><a href="{% url 'posts'%}">Back to main view</a></p>

<form action="" method="POST">
  {% csrf_token %} title: <br />
  <input type="text" name="title" placeholder=" {{ post.title }}" /><br /><br />
  <textarea name="text" id="" cols="30" rows="10" placeholder=" {{ post.text }}"></textarea><br />
  <input type="date" id="start" name="pub_date" value="2018-07-22" min="2018-01-01" max="2030-12-31">
  <br />
  <input type="submit" />
</form>
{% endblock %}

```

In `views.py`, add the logic to handle the blog post update

```python
def update_post(request, id):
    blog_post = Blog.objects.get(id=id)
    blog_post.title = request.POST['title']
    blog_post.text = request.POST['text']
    blog_post.pub_date = request.POST['pub_date']
    print(blog_post)
    blog_post.save()
    return redirect('posts')

```

In `urls.py` add a new route:

```python
    path('update_post/<int:id>', views.update_post, name = 'update_post')


```

Connect the form to the route! Go back to the `details.html`page and reference the route in the form action attribute:


```html

<form action="{%url 'update_post' post.id%}" method="POST">
```

You should now be able to update blog posts!

