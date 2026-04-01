temp = float(input("Введите температуру: "))

if temp < 10:
    print('Cold!')
elif 10 <= temp <= 24:
    print('Warm!')
else:
    print('Hot!')
