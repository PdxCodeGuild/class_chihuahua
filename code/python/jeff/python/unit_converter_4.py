distance_unit = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'km': 1000, 
}

distance_unit_2 = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'km': 1000, 
}

def unit_converter():
    distance_input = int(input('\nPlease enter the distance: \n'))
    unit_type = input('\nPlease enter the type of unit: ft for foot, mi for mile,\nme for meter, km for kilometer, yd for yard, in for inch : ')
    subtotal = distance_unit[unit_type] * distance_input
    distance_output = input('\nPlease enter the output units: \n')
    total = subtotal * distance_unit_2[distance_output]
    #input('n\Please enter the distance in feet') 
    return f"Your conversion is equal to {total} {distance_output} " 

distance_unit.update({'yd': 0.9144 , 'in': 0.0254})


print(unit_converter())

'''
1 yard is 0.9144 m
1 inch is 0.0254 m
> what are the input units? ft
> what are the output units? mi
'''