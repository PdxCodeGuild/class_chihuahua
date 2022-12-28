from optparse import Option
from flask import Flask, render_template, request
 
app = Flask(__name__)
form_data = {
'key1(field1_name)' : 'value1(username_value)',
'key2(field2_name)' : 'value2(field2_value)',
'key3(field3_name)' : 'value3(field3_value)'
}
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    elif request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data, options = Option)

if __name__=='__main__':
    app.run(debug=True)