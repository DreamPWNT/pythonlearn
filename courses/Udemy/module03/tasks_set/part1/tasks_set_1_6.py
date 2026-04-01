password = input("Введите пароль: ")

if len(password) < 6:
    print('Your password is too short. Need 6 or more symbols')
else:
    print('Password accepted!')
