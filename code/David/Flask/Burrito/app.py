from flask import Flask, render_template, request, redirect
import random
import string
app = Flask(__name__)



@app.route('/')
def path1():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    return render_template('order.html')

@app.route('/order-complete')
def complete():
    n = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return render_template('order-complete.html', res=res)
