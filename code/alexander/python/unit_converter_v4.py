conversions_list = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'in': 0.0254
}


unit_input = input(f'what are the input units? ')

quantity_input = int(input(f'what is the distance? '))

unit_output = input(f'what are the output units? ')

converting = conversions_list[unit_input]

middle_number = quantity_input * converting

end_number = middle_number * conversions_list[unit_output]

print(f'{quantity_input} {unit_input} is {end_number} m')