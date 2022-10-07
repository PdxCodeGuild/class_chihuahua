distance_unit = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'km': 1000, 
}

def unit_converter():
    distance_feet = int(input('\nPlease enter the distance in feet: \n'))
    unit_type = input('\nPlease enter the type of unit: ft for foot, mi for mile,\nme for meter, km for kilometer: ')
    total = distance_unit[unit_type] * distance_feet
    #input('n\Please enter the distance in feet') 
    return f"Your conversion is equal to {total} meters " 

print(unit_converter())
