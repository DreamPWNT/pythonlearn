import math

n = int(input('Enter sides quantity: '))
s = int(input('Enter side length: '))

area = (n * pow(s, 2)) / (4 * math.tan(math.pi / n))

print(f'Area of polygon = {area}')
