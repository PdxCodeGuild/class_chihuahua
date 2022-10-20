from flask import Flask, render_template, redirect, request
import requests
app = Flask(__name__)


@app.route('/')
def selection():
    cat_request = requests.get('https://api.thecatapi.com/v1/images/search')
    r_cat = cat_request.json()
    cat_image = r_cat[0]['url']
    
    return render_template('index.html', cat = cat_image)

@app.route('/results')
def results():
    random_request = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    r_data = random_request.json()['drinks'][0]
    r_data_name = r_data['strDrink']
    r_drink_catagory = r_data["strCategory"]
    r_drink_imgaine = r_data['strDrinkThumb']
    ingred_list = [
"strIngredient1",
"strIngredient2", 
"strIngredient3", 
"strIngredient4",
"strIngredient5",
"strIngredient6",
"strIngredient7",
"strIngredient8",
"strIngredient9",
"strIngredient10",
"strIngredient11",
"strIngredient12",
"strIngredient13",
"strIngredient14",
"strIngredient15"
]
    ingred_messure = [
"strMeasure1",
"strMeasure2",
"strMeasure3",
"strMeasure4",
"strMeasure5",
"strMeasure6",
"strMeasure7",
"strMeasure8",
"strMeasure9",
"strMeasure10",
"strMeasure11",
"strMeasure12",
"strMeasure13",
"strMeasure14",
"strMeasure15"]

    return render_template('results.html', r_data= r_data, r_data_name = r_data_name, r_drink_catagory = r_drink_catagory, ingred_messure = ingred_messure, ingred_list = ingred_list, r_drink_imgaine = r_drink_imgaine )

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)