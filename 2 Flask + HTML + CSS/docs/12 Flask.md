
# Flask

- [Introduction](#introduction)
- [Setup](#setup)
- [Routing](#routing)
- [Template Rendering](#template-rendering)
- [Static Files](#static-files)
- [Query Parameters](#query-parameters)


## Introduction

Flask is a light-weight web application framework written in Python. It performs essentially the same functions as Django, but whereas Django provides many features for you, Flask is bare-bones, and additional features must be installed or developed yourself. While developing your application, your computer will be both the client and the server. When you deploy your application, a dedicated machine will have a public IP address and can send and receive requests from anyone on the web.

## Setup

You can install Flask with `pip install flask`. The [official flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/) provides walkthrough of flask's major features.

Below is a minimal Flask application, it receives a request at `localhost:5000/` and returns a response that simply contains "Hello World!". Copy-paste this code into a file `app.py`.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

app.run(debug=True)
```


## Routing


You can specify multiple different paths

```python
from flask import Flask
app = Flask(__name__)

# localhost:5000
@app.route('/')
def path1():
    return 'you\'re home'

# localhost:5000/path1/
@app.route('/path2/')
def path2():
    return 'you\'re at path 2'

# localhost:5000/path2/
@app.route('/path2/')
def path3():
    return 'you\'re at path 3'

# localhost:5000/path2/path3/
@app.route('/path4/')
def path4():
    return 'you\'re at path 4'
```


You can specify a variable in the path

```python
from flask import Flask
app = Flask(__name__)

# localhost:5000/user/joe/
# localhost:5000/user/jane/
@app.route('/user/<string:username>/')
def show_user_profile(username):
    return f'Showing profile for {username}'

# localhost:5000/user/5/
# localhost:5000/user/656/
@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return f'Showing post with id {post_id}'

```

## Template Rendering

Building HTML with string operations is tedious, so Flask provides a way to use html templates to build data. The templates are html files with special syntax in their own folder which **must** be called `templates`.

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  name = 'bob'
  temperature = 67
  nums = [1, 2, 3]  
  return render_template('index.html', name=name, temperature=temperature, nums=nums)
```

```html
<p>Hello {{name}}</p>

{% if temperature < 50 %}
<p>cold</p>
{% elif temperature < 80 %}
<p>warm</p>
{% else %}
<p>hot</p>
{% endif %}

<ul>
  {% for num in nums %}
  <li>{{num}}</li>
  {% endfor %}
</ul>
```

## Static Files

Static files (css, js, images, etc) must be put in a folder called `static`. You can then render the url for them in the template with the code below. Read more about static files in the [official docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/static/).

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}"/>
```

## Base html

You can create a common html file that shared component with other html templates, so that you do not have to repeat HTML markup.

The example below is for a "base.html" file

```html
<!DOCTYPE html>
<html>
  <head>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}"
    />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/js/lightbox.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.8.2/css/lightbox.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>My Webpage</title>
  </head>

  <body>
    <div id="content">{% block content %} {% endblock %}</div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW"
      crossorigin="anonymous"
    ></script>
    <script src="{{ url_for('static', filename='main.js') }}"></script>
  </body>
</html>

```

Any other html file can source common elements from the base file with this syntax:

```html

{% extends "base.html" %} {% block content %}

<h1>Hello there</h1>
  
{% endblock %}

```

## Query Parameters

Query parameters can be received in the view using `request.args`


```python
# localhost:5000?name=joe
@app.route('/')
def index():
    print(request.args['name']) # joe
```

