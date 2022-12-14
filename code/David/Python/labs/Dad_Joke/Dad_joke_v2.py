import requests

url = "https://icanhazdadjoke.com/"


payload={}
headers = {'Accept': ('application/json')}

d_response = requests.request("GET", url, headers=headers, data=payload)
dad_joke = d_response.json()

c_response = requests.get('https://api.chucknorris.io/jokes/random')
c_joke = c_response.json()

num = 0

end_points = ['Dad Jokes', 'Chuck Norris']
for e in end_points:
    num += 1
    
    print(f'{num}.{e}\n')

start = 1
while start == 1:
    select = int(input('\nJoke End Point: '))
    while select == 1:
        d_select = int(input('''
        1. Display Joke by ID
        2. Give me a Random Joke
        3. Go back to the main menu
        '''))
        if d_select == 1:
            give_id = input('Enter The ID number of the joke: \n')
            id_url = f'https://icanhazdadjoke.com/j/{give_id}'
            d_response = requests.request("GET", id_url, headers=headers, data=payload)
            dad_joke_id = d_response.json()
            print(f"\n{dad_joke_id['joke']}\n")
        elif d_select == 2:
            print(f"\n{dad_joke['joke']}\n")
        elif d_select == 3:
            break
    
    while select == 2:
        c_select = int(input('''
        1. Give me a Random Joke
        2. Give me a list of Catagories
        3. GIve me a joke from a certain Catagory
        4. Back to main menu
        '''))
        if c_select == 1:
            print(f"\n{c_joke['value']}\n")
        
        elif c_select == 2:
            c_cats = requests.get('https://api.chucknorris.io/jokes/categories')
            c_cats_text = c_cats.json()
            for c in c_cats_text:
                print(c)
            
        elif c_select == 3:
            c_choose = input('Which Catagory would you like: ')
            select_c_cat =  requests.get(f'https://api.chucknorris.io/jokes/random?category={c_choose}')
            c_cat = select_c_cat.json()
            print(c_cat['value'])
        
        elif c_select == 4:
            break