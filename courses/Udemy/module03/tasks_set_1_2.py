age = int(input("Введите возраст: "))

if 0 <= age <= 12:
    print('Child')
elif 13 <= age <= 17:
    print('Teenager')
elif age >= 18:
    print('Adult')
else:
    print('Incorrect input', age)
