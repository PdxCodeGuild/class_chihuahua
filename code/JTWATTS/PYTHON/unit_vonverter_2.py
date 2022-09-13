distance = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
    # "yard": 0.9144,
    # "inch": 0.0254
    }

def unit_converter():
    conversion = input("what is the input units?  ")
    how_far = int(input('what is the distance?  '))
    output_unit = input("what are the output units? ")
    answer = how_far * distance[conversion] 
    print(f' {how_far} {conversion} is {answer} {output_unit}')
    
    # if conversion == mi:
    #     answer1 = how_far * 1609.34
    # answer = user1 * 0.3048
    # print(f' {user1} ft is {answer} m')

    



unit_converter()