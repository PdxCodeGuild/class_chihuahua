def unit_converter():
    initial_value = int(input("what is the distance?: "))
    input_units = input("what are the input units? (ft, mi, km, yd, in): ")
    converted_units = initial_value * input_units
    output_units = input("What are the output units? (ft, mi, km, yd, in): ")
    
    if input_units == "ft":
            output = 
            print(f"{initial_value} {input_units} is {.3048 * initial_value} {output_units}")

    # elif input_units == 'mi':
    #     print(f"{initial_value} {input_units} is {1609.34 * initial_value} {output_units}")
    # elif input_units == 'km':
    #     print(f"{initial_value} {input_units} is {1000 * initial_value} {output_units}")
    # elif input_units == 'yd':
    #     print(f"{initial_value} {input_units} is {.9144 * initial_value} {output_units}")
    # elif input_units == 'in':
    #     print(f"{initial_value} {input_units} is {.0254 * initial_value} {output_units}")

unit_converter()
