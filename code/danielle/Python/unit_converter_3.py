def unit_converter():
    initial_value = int(input("what is the distance?: "))
    initial_units = input("What are the units? (ft, mi, km, yd, in): ")
    if initial_units == 'ft':
        print(f"{initial_value} {initial_units} is {.3048 * initial_value} m")
    elif initial_units == 'mi':
        print(f"{initial_value} {initial_units} is {1609.34 * initial_value} m")
    elif initial_units == 'km':
        print(f"{initial_value} {initial_units} is {1000 * initial_value} m")
    elif initial_units == 'yd':
        print(f"{initial_value} {initial_units} is {.9144 * initial_value} m")
    elif initial_units == 'in':
        print(f"{initial_value} {initial_units} is {.0254 * initial_value} m")

unit_converter()