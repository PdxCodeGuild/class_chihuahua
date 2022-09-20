distance_unit = {
    'ft': 0.3048,
    'me': 1,
    'mi': 1609.34,
    'ki': 1000, 
    'In': 0.0254,
    'Yd': 0.9144
}

conversion = ()
type_of_unit = []

def unit_converter():
    distance_feet = float(input('\nPlease enter the distance:'))
    type_of_unit = input('\nPlease enter the type of unit: ft for foot, mi for mile,\nme for meter, ki for kilometer: ')
    conversion = distance_feet * type_of_unit   
    return f"Your conversion is equal to {conversion} meters " 

print(unit_converter)



''' if input.str.contains('ft'):
        total = foot_conversion * str(distance_feet)
    elif input.str.contains('mi'):
        total = mile_conversion * str(distance_feet)
    elif input.str.contains('km'):
        total = kilometer_conversion * str(distance_feet)
    elif input.str.contains('mi'):
        total = meter_conversion * str(distance_feet)
    return f"Your conversion is equal to {total} meters "  '''  
'''ft = foot_conversion
    mi = mile_conversion
    me = meter_conversion
    ki = kilometer_conversion'''
"""
remove before pushing the test

"""

#unit_converter()