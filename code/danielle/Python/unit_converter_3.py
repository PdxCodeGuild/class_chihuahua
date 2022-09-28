unit_converter = {
    "ft": .3048,
    "mi": 1609.34,
    "km": 1000,
    "yd": .9144,
}
distance = input("What is the distance?: ")
distance = int(distance)
units = input("What are the units? (ft, mi, km, yd, in): ")

print(f"{distance} {units} is {round(unit_converter[units] * distance, 4)} m")