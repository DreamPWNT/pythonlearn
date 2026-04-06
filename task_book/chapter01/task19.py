import math

FREE_ACCELERATION = 9.8

h = int(input("Enter height: "))

v = math.sqrt(2 * FREE_ACCELERATION * h)

print(f'Speed = {v}')
