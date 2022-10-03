def unit_converter():
    m = .3048
    initial_value = input("what is the distance in feet? ")
    converted_amount = int(initial_value) * m
    print(f"{initial_value} ft is {converted_amount} m")

unit_converter()
