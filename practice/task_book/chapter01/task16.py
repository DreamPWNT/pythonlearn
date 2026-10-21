import math

r = int(input('Enter radius value: '))

S = round(math.pi * pow(r, 2), 2)
V = round((4 / 3) * math.pi * pow(r, 3), 2)

print(f'S = {S}, V = {V}')
