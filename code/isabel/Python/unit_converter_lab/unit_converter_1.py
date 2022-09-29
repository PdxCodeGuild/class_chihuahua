def unit_converter():
    data_feet = input("What is distance in feet?  Please enter a number: ")
    data_meter = int(data_feet) * 0.3048
    answer = print(f"{data_feet} ft is {data_meter} m")
    return answer
    
unit_converter()