from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def order():
    if request.method == "GET":
        return render_template('burrito.html')
    elif request.method == "POST":
        name = request.form['name'] #text field
        email = request.form['email'] #text field
        tortilla = request.form['tortilla'] #radio buttons
        rice = request.form['rice'] #radio buttons
        beans = request.form['beans'] #radio buttons
        protein = request.form.getlist('protein') #check box
        extras = request.form.getlist('extras') #check box
        print('Hi,', name) 
        print('e-mail: ',email)
        print('You Ordered: ')
        print('tortilla: ', tortilla)
        print('rice: ', rice)
        print('beans: ',beans)
        print('protein: ',protein)
        print('extras: ',extras)
        return render_template('burrito.html', name=name, email=email, 
        tortilla=tortilla, rice=rice, beans=beans, protein=protein, extras=extras,)

       
        
app.run(debug=True)


    