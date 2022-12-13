from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
  name = 'bob'
  temperature = 67
  nums = [1, 2, 3]  
  return render_template('blog.html', name=name, temperature=temperature, nums=nums)

app.run(debug=True, port=80, host='localhost')