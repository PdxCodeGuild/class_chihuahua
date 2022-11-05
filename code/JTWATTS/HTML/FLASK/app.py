from flask import Flask, render_template, request
import requests


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method =='GET':

        tortilla = ['wheat', 'white', 'spinach', 'corn']
        rice = ['white', 'brown']
        beans = ['brown', 'black']
        meats = ['carnitas', 'sofritas', 'chicken']
        dairy = ['sour cream', 'cheese']
        sauce = ['guac', 'salsa']
        return render_template('burrito.html', meats = meats, rice = rice, beans = beans, tortilla = tortilla , dairy = dairy, sauce = sauce)
    elif request.method == 'POST':
        burrito = request.form.get('choice of ')
        print(burrito)
        return render_template('total_burrito.html')



app.run(debug=True)

