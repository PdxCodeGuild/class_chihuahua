def unit_converter():
    unit_in_feet = input("distance in feet: ")
    unit_in_meters = int(unit_in_feet) * 0.3048
    print(f"{unit_in_feet} ft is {unit_in_meters} meters.")


def unit_converter_2():
    distance = int(input('enter the distance: '))
    units = input('enter units: ')
    if units == "feet":
        meters = distance * 0.3048
        print(meters)
    elif units == "miles":
        meters = distance * 1609.34
        print(meters)
    elif units == "meters":
        meters = distance * 1
        print(meters)
    elif units == "kilometers":
        meters = distance * 1000
        print(meters)
    elif units == "yards":
        meters = distance * 0.9144
        print(meters)
    elif units == 'inches':
        meters = distance * 0.0254
        print(meters)

# unit_converter_2()

def unit_converter_3():
    distance = input("enter distance: ")
    input_unit = input('what is the input unit: ')
    output_unit = input('what is output unit: ')
    if input_unit == output_unit:
        print(distance)
        # this is for the times where input and output are the same unit, no operations nescessary 
    if input_unit == 'feet':
        distance_in_meters = int(distance) * 0.0348
        if output_unit == "meters":
            print(distance_in_meters)
        elif output_unit == "miles":
            distance_in_miles = int(distance_in_meters) * 1609.34
            print(distance_in_miles)
        elif output_unit == 'kilometers':
            distance_in_kilometers = distance_in_meters * 1000
            print(distance_in_kilometers)
    if input_unit == 'miles':
        distance_in_meters = int(distance) / 1609
        if output_unit == 'meters':
            print(distance_in_meters)
        elif output_unit == 'feet':
            distance_in_feet = int(distance_in_meters) * 0.3048
            print(distance_in_feet)
        elif output_unit == "kilometers":
            distance_in_kilometers = int(distance_in_meters) * 1000
            print(distance_in_kilometers)
    if input_unit == 'kilometers':
        distance_in_meters = int(distance) / 1000
        if output_unit  == 'meters':
            print(distance_in_meters)
        elif output_unit == 'feet':
            distance_in_feet = int(distance_in_meters) * 0.3048
            print(distance_in_feet)
        elif output_unit == 'miles':
            distance_in_miles == distance_in_meters * 1609.34
            print(distance_in_miles)
    if input_unit == "meters":
        distance_in_meters = distance
        if output_unit == 'feet':
            distance_in_feet = int(distance_in_meters) * 0.3048
            print(distance_in_feet)
        elif output_unit == "kilometers":
            distance_in_kilometers = int(distance_in_meters) * 1000
            print(distance_in_kilometers)
        elif output_unit == "miles":
            distance_in_miles = int(distance_in_meters) * 1609.34
            print(distance_in_miles)
