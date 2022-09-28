'''unit = {
    'F': 0.3048,
    'M': 1,
    'Mi': 1609.34,
    'Km': 1000, 
    'In': 0.0254,
    'Yd': 0.9144
}'''



def unit_converter():
    distance_feet = int(input('\nPlease enter the distance in feet: \n'))
    #input('n\Please enter the distance in feet') 
    meter_conversion = 0.3048
    total = meter_conversion * distance_feet
    return f"Your conversion is equal to {total} meters "   

print(unit_converter())



"""
remove before pushing the test

"""

#unit_converter()