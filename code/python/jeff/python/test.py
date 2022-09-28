distance_unit = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'km': 1000, 
}

distance_feet = str(input('\nPlease enter the distance:'))
distance_unit = input('\nPlease enter the type of unit: ft for foot, mi for mile,\nme for meter, km for kilometer: ')


print(distance_feet * distance_unit[key])