import math

a = float(input('Enter "a" coefficient of square equation: '))
b = float(input('Enter "b" coefficient of square equation: '))
c = float(input('Enter "c" coefficient of square equation: '))

D = pow(b, 2) - 4 * a * c

if D < 0:
    print(f'Square equation {a}x^2+({b}x)+({c}) = 0 has no roots')
elif D == 0:
    x = -b / (2 * a)

    print(f'Square equation {a}x^2+({b}x)+({c}) = 0 has one root. x = {x}')
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    print(
        f'Square equation {a}x^2+({b}x)+({c}) = 0 has two roots. x1 = {x1}, x2 = {x2}')
