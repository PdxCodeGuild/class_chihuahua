feet_inbound = int(input("what is the distance in feet?"))

def unit_converter(feet_inbound):
    return feet_inbound * 0.3048
    
print(f"{feet_inbound} ft is {unit_converter(feet_inbound)} meters")
