num = float(input("Введите число: "))

if 0 <= num <= 100:
    print(round(num, 2))
else:
    print('Enter num between 0 and 100')
