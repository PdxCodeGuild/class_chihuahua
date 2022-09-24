unit_types = {
     "feet": 0.3048,
     "miles": 1609.34,
     "meters": 1,
     "kilometers": 1000,
     "yards": 0.9144,
     "inches": 0.0254
}

def unit_converter():
    distance = float(input("What is the distance?: "))
    units = input("What are the input units?: ")
    output_units = input("What are the output units?: ")
    from_user_inputs = unit_types[units]
    to_user_outputs = unit_types[output_units]
    new_value = (distance * (from_user_inputs / to_user_outputs))

    return f"{new_value} {output_units}"

print(unit_converter())