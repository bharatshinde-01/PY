# Write python script using package to calculate area and perimeter of circle
import math
r = float(input("Enter radus of circle :"))
area = math.pi * r * r
parameter = 2 * math.pi * 4
print("Area of circle is :",round(area,2))
print("Perimeter of circle is :",round(parameter,2))
