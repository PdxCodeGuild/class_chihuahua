while True:
    unit_dict = {
        'ft': 0.3048,
        'mi': 1609.34,
        'km': 1000,
        'yd': 0.9144,
        'm': 1,
        'in': 0.0254
    }
    Many_distance = int(input("How much distance? "))
    starting_unit = input("Which unit to start with? ")
    which_unit = input("Which unit? ")

    total = unit_dict[starting_unit] / unit_dict[which_unit] * Many_distance
    print(f"{Many_distance} {starting_unit} is equal to {round(total, 2)} {which_unit} ")
    play_again = input("Would you like to play again? ")
    if play_again == "no":
        break