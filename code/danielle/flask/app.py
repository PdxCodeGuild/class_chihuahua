from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Danielle'
    temperature = 67
    nums = [1, 2, 3]
    return render_template('index.html', name=name, temperature=temperature, nums=nums)

################################################
#from flask import Flask
#app = Flask(__name__)

# @app.route('/user/<string:username>/')
# def show_user_profile(username):
#     return f'Showing profile for {username}'

# @app.route('/post/<int:post_id>/')
# def show_ost(post_id):
#     return f'Showing post with id {post_id}'
#################################################
#@app.route('/') #with route, specify address in Flask
#def index():
#     name = "danielle"
#     temperature =  67
#     nums = [1,2,3]

    #return "Hello World!"
    #render_template('index.html')

# @app.route('/path2/<string:username>')
# def path_2():
#     return 'Another new route!'

# @app.route('/path3/<int:post_id>')
# def path_3():
#     return 'One last route!'
# app.run(debug=True)
##############################

# create a base HTML for structure of website - elements should be repeated through website, like navigation. 

# {% extends 'base.html' %}
# {% block content %}

# <h1>Main Page</h1>

# {% endblock %}
