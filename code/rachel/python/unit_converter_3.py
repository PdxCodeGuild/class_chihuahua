# create dictionary and add items. The key is unit to be converted and the value is the conversion rate to convert the unit to meters.

meter = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yard': 0.9144, # added to version 3
    'inch': 0.0254  #added to version 3
}

# initialize variable 'unit' and the use the input() function to ask the user to specify the unit they are wanting to convert to meters.
unit = input("What unit do you want to convert to meters? ")
# initialize variable 'initial_value' to hold the distance the user wants to convert. Use the input() to get the 'initial_value'. 
initial_value = input("What is the distance (number only)? ")
# convert the user input from a string to a float so that it can be converted
initial_value = float(initial_value)
# initialize variable 'conversion' that will get the correct conversion rate for the unit entered by the user
conversion = meter[unit]

# define a function and assign parameters
def unit_converter(initial_value, conversion):
    # manipulate the parameters by multiplying them
    result = initial_value * conversion
    # return the result of multiplying the parameters
    return result
    

result = unit_converter(initial_value, conversion)
# display the initial inputted value and the unit type and that value converted to meters and rounded to 4 decimal places
print(f"{initial_value} {unit} is {round(result, 4)} meters.")


