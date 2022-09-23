def unit_converter():
    input_value = input("what is the distance?: ")
    input_units = input("what are the input units? (ft, mi, km, yd, in): ")
    output_units = input("What are the desired output units? (ft, mi, km, yd, in): ")
    converted_units = {
        "ft": .3048, 
        "mi": 1609.34, 
        "km": 1000, 
        "yd": .9144, 
        "in": .0254, 
        }
    input_to_meters = float(input_value) * float(converted_units[input_units])
    meters_to_output = float(input_to_meters) / float(converted_units[output_units])
    print(meters_to_output)

unit_converter()