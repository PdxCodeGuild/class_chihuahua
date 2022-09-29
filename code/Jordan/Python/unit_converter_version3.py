def unit_converter():
    distance = input("What is the distance?: ")
    units = input("What are the units?: ")
    distance = float(distance)
    feet = 0.3048
    miles = 1609.34
    meters = 1
    kilometers = 1000
    yards = 0.9144
    inches = 0.0254
    if units == "feet":
        distance_converted = distance * feet
    elif units == "miles":
        distance_converted = distance * miles
    elif units == "meters":
        distance_converted = distance * meters
    elif units == "inches":
        distance_converted = distance * inches
    elif units == "yards":
        distance_converted = distance * yards
    elif units == "kilometers":
        distance_converted = distance * kilometers
    fun_return = (f"initial value {distance} is {distance_converted} meters")
    return print(fun_return)
unit_converter()