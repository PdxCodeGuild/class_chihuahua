class Rectangle:
    def perimeter(length, width):
        perimeter = int(length) + int(width)
    def area(length, width):
        area = int(length) * int(width)
        
Measurement = Rectangle
Measurement.perimeter(5, 6)
Measurement.area(4, 5)

print(Measurement)
