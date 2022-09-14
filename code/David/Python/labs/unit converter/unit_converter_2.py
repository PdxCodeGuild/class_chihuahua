while True:
    unit_dict = {
        'ft': 0.3048,
        'mi': 1609.34,
        'km': 1000,
        'm': 1,
    }
    
    Many_distance = int(input("How much distance? "))
    which_unit = input("Which unit? ")

    total = Many_distance * unit_dict[which_unit]
    print(f"{Many_distance} {which_unit} is equal to {round(total, 2)} meters ")
    play_again = input("Would you like to play again? ")
    if play_again == "no":
        break