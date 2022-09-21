def unit_converter():
    input_value = (input("what is the distance?: "))
    input_units = input("what are the input units? (ft, mi, km, yd, in): ")
    output_units = input("What are the desired output units? (ft, mi, km, yd, in): ")
    input_units_to_meters = {
        "ft": int(input_value) * .3048, 
        "mi": int(input_value) * 1609.34, 
        "km": int(input_value) * 1000, 
        "yd": int(input_value) * .9144, 
        "in": int(input_value) * .0254, 
        }
    output_units_to_meters = {
        "ft": int(input_value) * .3048, 
        "mi": int(input_value) * 1609.34, 
        "km": int(input_value) * 1000, 
        "yd": int(input_value) * .9144, 
        "in": int(input_value) * .0254,
    }
    if output_units == "ft":
        print(f"{input_value} {input_units} is {input_units_to_meters * output_units_to_meters} {output_units}")

unit_converter()

            # m_mi = "mi" * 1609.34
            # m_km = "km" * 1000
            # m_yd = "yd" * .9144
            # m_in = "in" * .0254