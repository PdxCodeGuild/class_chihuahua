# create dictionary and add items. The key is unit to be converted and the value is the conversion rate to convert the unit to meters.

meter = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': 0.9144, # added to version 3
    'inches': 0.0254  #added to version 3
}

# initialize variable 'unit' and the use the input() function to ask the user to specify the unit they are wanting to convert to meters.
input_unit = input("What unit are you converting from? ")
# initialize variable 'initial_value' to hold the distance the user wants to convert. Use the input() to get the 'initial_value'. 
output_unit = input("What unit are you converting to? ")
initial_value = input("What is the distance (number only)? ")
# convert the user input from a string to a float so that it can be converted
initial_value = float(initial_value)
# initialize variable 'm_conversion' that will get the correct conversion rate to convert the distance in the input unit to meters
m_conversion = meter[input_unit]
# initialize variable 'output_conversion' that will get the correct conversion rate to convert the distance in meters to the distance in the output unit
output_conversion = meter[output_unit]

# define a function that will convert the input distance and unit to meters and then from meters to the requested output unit. The function has three parameters.
def unit_converter(initial_value, m_conversion, output_conversion):
    # manipulate the parameters by multiplying them
    m_result = initial_value * m_conversion
    output_result = m_result / output_conversion
    # return the result of multiplying the parameters
    return output_result
    
# display the initial inputted value and unit and then use the defined function to display the initial values converted to the requested unit to 4 decimal places
print(f"{initial_value} {input_unit} is {round(unit_converter(initial_value, m_conversion, output_conversion), 4)} {output_unit}.")


