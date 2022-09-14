unit_converter = {
    "ft": .3048,
    "mi": 1609.34,
    "km": 1000,
}
distance = input("What is the distance?: ")
distance = int(distance)
units = input("What are the units? (ft, mi, km): ")

print(f"{distance} {units} is {round(unit_converter[units] * distance, 4)} m")