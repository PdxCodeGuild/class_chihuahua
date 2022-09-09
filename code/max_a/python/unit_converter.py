units_to_meters = {
     'feet': 0.3048,
     'miles': 1609.34,
     'meters': 1,
     'kilometers': 1000,
     'yards': 0.9144,
     'inches': 0.0254
    }

def unit_converter():
    distance = int(input("Distance: "))
    unit1 = input("Units From: ")
    unit2 = input("Units To: ")
    meters = distance * units_to_meters[unit1]
    return f"{distance} {unit1} is {meters/units_to_meters[unit2]} {unit2}."

"""
converts chosen units to chosen units
"""

print(unit_converter())