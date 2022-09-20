distance_unit = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'km': 1000, 
}

def unit_converter():
    distance_feet = int(input('\nPlease enter the distance in feet: \n'))
    unit_type = input('\nPlease enter the type of unit: ft for foot, mi for mile,\nme for meter, km for kilometer, yd for yard, in for inch : ')
    total = distance_unit[unit_type] * distance_feet
    #input('n\Please enter the distance in feet') 
    return f"Your conversion is equal to {total} meters " 

distance_unit.update({'yd': 0.9144 , 'in': 0.0254})


print(unit_converter())

'''
1 yard is 0.9144 m
1 inch is 0.0254 m
'''