import random

def pick6():
    winning = []
    n = 6
    for i in range(n):
        winning.append(random.randint(1,100))
    print(winning)
    ticket = input("Choose 6 numbers (1-99), separated by a comma and space: ")
    print(ticket)

    def num_matches(winning, ticket):
        for winning in ticket:
            if winning == ticket:
                print("Your ticket matches the winning ticket")
    
    num_matches(winning, ticket)

pick6()
