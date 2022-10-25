def unit_converter():
    input_value = input("what is the distance?: ")
    input_units = input("what are the input units? (ft, mi, m, km): ")
    output_units = input("What are the desired output units? (ft, mi, m, km): ")
    converted_units = {
        "ft": .3048, 
        "mi": 1609.34,
        "m": 1, 
        "km": 1000,  
        }
    input_to_meters = float(input_value) * float(converted_units[input_units])
    meters_to_output = float(input_to_meters) / float(converted_units[output_units])
    return(meters_to_output)
    
print(unit_converter())
