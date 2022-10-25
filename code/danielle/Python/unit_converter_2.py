def unit_converter():
    initial_value = int(input("what is the distance?: "))
    initial_units = input("What are the units? (ft, mi, km): ")
    if initial_units == 'ft':
        print(f"{initial_value} {initial_units} is {.3048 * initial_value} m")
    elif initial_units == 'mi':
        print(f"{initial_value} {initial_units} is {1609.34 * initial_value} m")
    elif initial_units == 'km':
        print(f"{initial_value} {initial_units} is {1000 * initial_value} m")

unit_converter()


#def fizz_buzz():
#  for num in range(0,100):
#    if num % 5 == 0 and num % 3 == 0:
#      print(num, "fizzbuzz")
#    elif num % 3 == 0:
#      print(num, "fizz")
#    elif num % 5 == 0:
#      print( num, "buzz")

#fizz_buzz()

