from flask import Flask, render_template, request
app = Flask(__name__)
'''
@app.route("/")
def index():
        return render_template("index.html")
'''
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        tortilla = request.form['tortillaradio']
        rice = request.form['riceradio']
        beans = request.form['beansradio']
        protein = request.form['proteinradio']
        additional = request.form['additionalcheck']
        instructions = request.form['instructions']
        return render_template("success.html")


@app.route("/success", methods=['POST'])
def success():
    return render_template('success.html')

'''
@app.route("/orderfood")
def orderfood():
    return render_template("success.html")
'''

app.run(debug=True)