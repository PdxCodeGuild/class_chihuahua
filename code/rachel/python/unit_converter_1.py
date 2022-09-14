# initialize variable and ask for user input for the value
initial_value = input("What is the distance in feet: ")
# convert the user input from a string to a float so that it can be converted
initial_value = float(initial_value)
# initialize another variable with a set value of 1 ft in meters
conversion = 0.3048

# define a function and assign parameters
def unit_converter(initial_value, conversion):
    # manipulate the parameters by multiplying them
    result = initial_value * conversion
    # return the result of multiplying the parameters
    return result


result = unit_converter(initial_value, conversion)

# display the initial inputted value in feet and that value converted to meters and rounded to 4 decimal places
print(f"{initial_value} feet is {round(result, 4)} meters.")

