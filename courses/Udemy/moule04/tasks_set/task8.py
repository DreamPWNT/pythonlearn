password = input("Введите пароль: ")

while True:
    if password != 'python':
        print('Wrong password, try again')

        password = input("Введите пароль: ")
    else:
        print('Access granted!')

        break
