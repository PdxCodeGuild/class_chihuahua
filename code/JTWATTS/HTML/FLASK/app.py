from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    tortilla = ['wheat', 'white', 'spinach', 'corn']
    rice = ['white', 'brown']
    beans = ['brown', 'black']
    meats = ['carnitas', 'sofritas', 'chicken']
    dairy = ['sour cream', 'cheese']
    sauce = ['guac', 'salsa']
    return render_template('burrito.html', meats = meats, rice = rice, beans = beans, tortilla = tortilla , dairy = dairy, sauce = sauce)

@app.route('//')
def about():
    return render_template('style.css')

# @app.route('//')
# def index():
#     tortilla = ['wheat', 'white', 'spinach', 'corn']
#     return render_template('base.html', tortilla = tortilla)

# @app.route('/meat/')
# def path2():
#     return 'THE MEATS'  

app.run(debug=True)




# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def index():
#   name = 'bob'
#   temperature = 67
#   nums = [1, 2, 3]  
#   return render_template('index.html', name=name, temperature=temperature, nums=nums)

# @app.route('/')
# def index():
#     return 'Is this me?'

# localhost:5000
# @app.route('/')
# def path1():
#     return 'TORTIA'

# # localhost:5000/path1/
# @app.route('/path2/')
# def path2():
#     return 'THE MEATS'

# # localhost:5000/path2/
# @app.route('/path3/')
# def path3():
#     return 'THE DAIRY'

# # localhost:5000/path2/path3/
# @app.route('/path4/')
# def path4():
#     return 'THE VEGGIES'   

# @app.route('/path5/')
# def path4():
#     return 'THE SAUCE'     


