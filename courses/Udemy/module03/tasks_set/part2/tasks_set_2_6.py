name = input("Введите имя: ")
surname = input("Введите фамилию: ")

if len(name) > 0 and len(surname) > 0:
    print(f'Hello, {name} {surname}')
else:
    print('Incorrect input, fill all values!')
