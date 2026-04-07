a = int(input('Enter first triangle side length: '))
b = int(input('Enter second triangle side length: '))
c = int(input('Enter third triangle side length: '))

if a != b and b != c and a != c:
    print('A versatile triangle')
elif a == b == c:
    print('An equilateral triangle')
else:
    print('An isosceles triangle')
