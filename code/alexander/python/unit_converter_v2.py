conversions_list = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}


unit_input = input(f'what are the input units? ')

quantity_input = int(input(f'what is the distance? '))

converting = conversions_list[unit_input]

end_number = quantity_input * converting

print(f'{quantity_input} {unit_input} is {end_number} m')