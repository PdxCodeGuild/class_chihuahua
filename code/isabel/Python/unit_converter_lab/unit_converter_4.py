from lib2to3.pytree import convert


data = input("Please enter a number: ")
data_units = input("Please enter units (m, km, mi, ft, yd, in) of number: ")
convert_units = input("Please enter units to convert to (m, km, mi, ft, yd, in): ")
data_flo = float(data)

def unit_convert_units():
    

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
        elif data_units == 'mi' and convert_units == 'm':
            answer = data_flo * 1609.34
            return f"{answer} m"
        elif data_units == 'mi' and convert_units == 'km':
            answer = data_flo * (1609.34/1000)
            return f"{answer} km"
        elif data_units == 'mi' and convert_units == 'ft':
            answer = data_flo * (1609.34/0.3048)
            return f"{answer} ft"
        elif data_units == 'yd' and convert_units == 'm':
            answer = data_flo * 0.9144
            return f"{answer} m"
        elif data_units == 'm' and convert_units == 'yd':
            answer = data_flo * (1/0.9144)
            return f"{answer} yd"
        elif data_units == 'ft' and convert_units == 'yd':
            answer = data_flo * (12 * 0.0254)
            return f"{answer} yd"
        elif data_units == 'yd' and convert_units == 'ft':
            answer = data_flo * (1/(12 * 0.0254))
            return f"{answer} ft"
        elif data_units == 'yd' and convert_units == 'mi':
            answer = data_flo * (0.9144/1609.34)
            return f"{answer} mi"
        elif data_units == 'mi' and convert_units == 'yd':
            answer = data_flo * (1609.34/0.9144)
            return f"{answer} yd"
        elif data_units == 'yd' and convert_units == 'in':
            answer = data_flo * (0.9144/0.0254)
            return f"{answer} in"
        elif data_units == 'in' and convert_units == 'yd':
            answer = data_flo * (0.0254/0.9144)
        elif data_units == 'yd' and convert_units == 'km':
            answer = data_flo * (0.9144/1000)
            return f"{answer} km"
        elif data_units == "km" and convert_units == "yd":
            answer = data_flo * (1000/0.9144)
            return f"{answer} yd"
        elif data_units == "in" and convert_units == "ft":
            answer = data_flo * (1/12)
            return f"{answer} ft"
        elif data_units == "ft" and convert_units == "in":
            answer = data_flo * 12
            return f"{answer} in"
        elif data_units == "in" and convert_units == "mi":
            answer = data_flo * (0.0254/1609.34)
            return f"{answer} mi"
        elif data_units == "mi" and convert_units == "in":
            answer = data_flo * (1609.34/0.0254)
            return f"{answer} in"
        elif data_units == "in" and convert_units == "m":
            answer = data_flo * (0.0254)
            return f"{answer} m"
        elif data_units == "m" and convert_units == "in":
            answer = data_flo * (1/0.0254)
            return f"{answer} in"
        elif data_units == "in" and convert_units == "km":
            answer = data_flo * (0.0254/1000)
            return f"{answer} km"
        elif data_units == "km" and convert_units == "in":
            answer = data_flo * (1000/0.0254)
            return f"{answer} in"

print(f"{data_flo} {data_units} is {unit_convert_units()}")


