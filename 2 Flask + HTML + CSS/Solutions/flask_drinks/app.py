from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/drinks/', methods=["GET", "POST"])
def drinks():
    if request.method == "GET":
        list_ingredients = ["Gin", "Vodka", "Rum", "Tequila", "Whiskey", "Cognac" ]
        return render_template('drinks.html', list_ingredients=list_ingredients)
    elif request.method == "POST":
        ingredient = request.form.get('ingredients')
        response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient}')
        data = response.json()
        drinks = data['drinks']
        print(drinks)
        return render_template('cocktails_list.html', drinks=drinks)


app.run(debug=True)