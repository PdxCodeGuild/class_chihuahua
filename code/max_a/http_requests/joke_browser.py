import requests
import os
from time import sleep

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_page(t, l, p):
    response = requests.get(f'https://icanhazdadjoke.com/search', params={'term': t, 'limit': l, 'page': p,}, headers={'accept': 'application/json'})
    res_json = response.json()
    print(f"--- Jokes about \"{t}\" ---")
    for joke in res_json['results']:
        print(joke['joke'])
        print(f"({joke['id']})\n")
        sleep(0.1)
    print(f"--- Displaying page {res_json['current_page']} of {res_json['total_pages']} ---")
    return res_json

term = input("Search for what term?\n")
limit = 5
page = 1

while True:
    clear()
    most_recent = display_page(term, limit, page) # sends request, displays the jokes, and stores the response for info needed in the loop
    instruction = input("What would you like to do? (next, previous, search, limit, quit)\n")
    if instruction == 'next':
        if most_recent['total_pages'] > most_recent['current_page']:
            page += 1
        else:
            print("That was the last page.")
    elif instruction == 'previous':
        if most_recent['current_page'] > 1:
            page -= 1
        else:
            print("That was the first page.")
    elif instruction == 'search':
        term = input("Search for what term?\n")
        page = 1 # otherwise you may end up with a current_page value higher than the total_page value, which always returns nothing
    elif instruction == 'limit':
        limit_change = input("How many jokes do you want to see per page?\n")
        try:
            limit = int(limit_change)
        except ValueError:
            print(f"{limit_change} is not a number!")
    elif instruction == 'quit':
        quit()
    sleep(1)
