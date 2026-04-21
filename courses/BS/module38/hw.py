while True:
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
    except ValueError as e:
        print(e)
        print('Enter only numbers!!!')
        continue

    try:
        div = a / b
    except ZeroDivisionError as e:
        print(e)
        print('Division by zero!!!!!')
        continue

    print(f'Result of {a} / {b} is: {div}')

    next_step = input('Dow you want to continue? ')

    if next_step == 'no':
        break
