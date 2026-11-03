import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

tsa = 2 * math.pi * r * (r + h)

volume = math.pi * r * r * h

print("Surface Area:", tsa)
print("Volume:", volume)