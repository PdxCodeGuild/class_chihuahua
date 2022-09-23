def unit_converter():
    input_value = input("what is the distance?: ")
    input_units = input("what are the input units? (ft, mi, km, yd, in): ")
    output_units = input("What are the desired output units? (ft, mi, km, yd, in): ")
    input_units_to_meters = {
        "ft": .3048, 
        "mi": 1609.34, 
        "km": 1000, 
        "yd": .9144, 
        "in": .0254, 
        }
    output_units_to_meters = {
        "ft": 3.28084, 
        "mi": .000621, 
        "km": .001, 
        "yd": 1.093613, 
        "in": 39.37008,
    }
    converted_units_ft_to_mi = (float(input_value)) * (float(input_units_to_meters["ft"])) * (float(output_units_to_meters["mi"]))
    print(f"{input_value} {input_units} is {converted_units_ft_to_mi} {output_units}")
    converted_units_ft_to_km = (float(input_value)) * (float(input_units_to_meters["ft"])) * (float(output_units_to_meters["km"]))
    print(f"{input_value} {input_units} is {converted_units_ft_to_km} {output_units}")
    converted_units_ft_to_yd = (float(input_value)) * (float(input_units_to_meters["ft"])) * (float(output_units_to_meters["yd"]))
    print(f"{input_value} {input_units} is {converted_units_ft_to_yd} {output_units}")
    converted_units_ft_to_in = (float(input_value)) * (float(input_units_to_meters["ft"])) * (float(output_units_to_meters["in"]))
    print(f"{input_value} {input_units} is {converted_units_ft_to_in} {output_units}")

    converted_units_mi_to_ft = (float(input_value)) * (float(input_units_to_meters["mi"])) * (float(output_units_to_meters["ft"]))
    print(f"{input_value} {input_units} is {converted_units_mi_to_ft} {output_units}")
    converted_units_mi_to_km = (float(input_value)) * (float(input_units_to_meters["mi"])) * (float(output_units_to_meters["km"]))
    print(f"{input_value} {input_units} is {converted_units_mi_to_km} {output_units}")
    converted_units_mi_to_yd = (float(input_value)) * (float(input_units_to_meters["mi"])) * (float(output_units_to_meters["yd"]))
    print(f"{input_value} {input_units} is {converted_units_mi_to_yd} {output_units}")
    converted_units_mi_to_in = (float(input_value)) * (float(input_units_to_meters["mi"])) * (float(output_units_to_meters["in"]))
    print(f"{input_value} {input_units} is {converted_units_mi_to_in} {output_units}")

    converted_units_km_to_ft = (float(input_value)) * (float(input_units_to_meters["km"])) * (float(output_units_to_meters["ft"]))
    print(f"{input_value} {input_units} is {converted_units_km_to_ft} {output_units}")
    converted_units_km_to_mi = (float(input_value)) * (float(input_units_to_meters["km"])) * (float(output_units_to_meters["mi"]))
    print(f"{input_value} {input_units} is {converted_units_km_to_mi} {output_units}")
    converted_units_km_to_yd = (float(input_value)) * (float(input_units_to_meters["km"])) * (float(output_units_to_meters["yd"]))
    print(f"{input_value} {input_units} is {converted_units_km_to_yd} {output_units}")
    converted_units_km_to_in = (float(input_value)) * (float(input_units_to_meters["km"])) * (float(output_units_to_meters["in"]))
    print(f"{input_value} {input_units} is {converted_units_km_to_in} {output_units}")

    converted_units_yd_to_ft = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["ft"]))
    print(f"{input_value} {input_units} is {converted_units_yd_to_ft} {output_units}")
    converted_units_yd_to_mi = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["mi"]))
    print(f"{input_value} {input_units} is {converted_units_yd_to_mi} {output_units}")
    converted_units_yd_to_km = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["km"]))
    print(f"{input_value} {input_units} is {converted_units_yd_to_km} {output_units}")
    converted_units_yd_to_in = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["in"]))
    print(f"{input_value} {input_units} is {converted_units_yd_to_in} {output_units}")

    converted_units_in_to_ft = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["ft"]))
    print(f"{input_value} {input_units} is {converted_units_in_to_ft} {output_units}")
    converted_units_in_to_mi = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["mi"]))
    print(f"{input_value} {input_units} is {converted_units_in_to_mi} {output_units}")
    converted_units_in_to_km = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["km"]))
    print(f"{input_value} {input_units} is {converted_units_in_to_km} {output_units}")
    converted_units_in_to_yd = (float(input_value)) * (float(input_units_to_meters["yd"])) * (float(output_units_to_meters["yd"]))
    print(f"{input_value} {input_units} is {converted_units_in_to_yd} {output_units}")

unit_converter()