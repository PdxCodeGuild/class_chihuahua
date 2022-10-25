from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# localhost:5000
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/receive_form/', methods=['POST'])
# def temperature():
#     print(request.form) # {'person_name': 'Jane', 'person_age': 34}
#     person_name = request.form['person_name'] # Jane
#     tortillaValue = request.form['tortillaValue'] # 34
#     print(tortillaValue)
#     return redirect('/')