import math

h = int(input('Enter cylinder height: '))
r = int(input('Enter cylinder radius: '))

v = round(h * math.pi * pow(r, 2), 1)

print(f'Cylinder volume = {v}')
