def unit_converter():
    distance = input("What is the distance in feet?: ")
    distance = float(distance)
    feet = 0.3048
    distance_converted = distance * feet
    fun_return = (f"initial value {distance} is {distance_converted} meters")
    return print(fun_return)
unit_converter()