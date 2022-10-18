from types import MethodDescriptorType


distance = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
    }

def unit_converter():
    how_far = int(input('what is the distance?  '))
    conversion = input("what is the input units?  ")
    output_unit = input("what are the output units? ")
   
    new_tot = how_far * distance[conversion]    
    drillz = new_tot / distance[output_unit]
    
    print(f' {how_far} {conversion} is {drillz} {output_unit}')

unit_converter()

    # from_who_to_what = trying / distance[output_unit]
        
    # answer = how_far * new_conver 
    #output = answer * distance[output_unit]
         #oldlenth x conv = new total times new conv
         #how_far * distance[conversion] * distance[output_unit]
         #new_tot * distance[output_unit]
        

 # if conversion == "ft":
    #    new_conver = distance[conversion] * 0.3048
    # elif conversion == "mi":
    #    new_conver = distance[conversion] * 1609.34
    # # elif conversion == "yard":
    # #     new_conver = distance[conversion] * 1
    # elif conversion == "km":
    #     new_conver == distance[conversion] * 1
    # elif conversion == "m":
    #     new_conver == distance[conversion] /1609.34

    # elif conversion == ""             or "mi" or "m" or "yard" and output_unit == "km" or "m" :
#   how do I convert everyting into MethodDescriptorType

    # take input and times it by m to a new veriabla then we multiply new var by output_unit
    #     new_conver = distance[conversion] / 1609.34
    # else:
    #     new_conver = distance[conversion] * 0.3048    

    # trying = distance[conversion]
    # if output_unit == distance.keys() is ("ft" or "mi"):
   # answer = how_far * new_conver
    # else:    # "yard": 0.9144,
    # "inch": 0.0254