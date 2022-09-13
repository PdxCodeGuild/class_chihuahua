def unit_convert_units():
    data = input("Please enter a number: ")
    data_units = input("Please enter units (m, km, mi, ft) of number: ")
    convert_units = input("Please enter units to convert to: ")
    data_flo = float(data)

    if data_units == convert_units:
        return data_flo + data_units
    else:

        if data_units == 'ft' and convert_units == 'm':
            answer = data_flo * 0.3048
            return f"{answer} m"
            
        elif data_units == 'ft' and convert_units == 'mi':
            answer = data_flo * (0.3048/1609.34)
            return f"{answer} mi"
        elif data_units == 'ft' and convert_units == 'km':
            answer =  data_flo * (0.3048/1000)
            return f"{answer} km"
        elif data_units == 'm' and convert_units == 'ft':
            answer = data_flo / 0.3048
            return f"{answer} ft"
        elif data_units == 'm' and convert_units == 'mi':
            answer = data_flo / 1609.34
            return f"{answer} mi"
        elif data_units == 'm' and convert_units == 'km':
            answer = data_flo / 1000
            return f"{answer} km"
        elif data_units == 'km' and convert_units == 'ft':
            answer = data_flo * (0.3048/1000)
            return f"{answer} ft"
        elif data_units == 'km' and convert_units == 'm':
            answer = data_flo * 1000
            return f"{answer} m"
            



print(unit_convert_units())

        

