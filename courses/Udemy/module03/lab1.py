print('Welcome to calculator!')

operation = input('Enter operation: ')
num1 = float(input('Enter first num: '))
num2 = float(input('Enter second num: '))
flag = True

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/' or operation == '//' or operation == '%':
    if num2 == 0:
        flag = False

        print('Division by zero is invalid!')
    else:
        if operation == '/':
            result = num1 / num2
        elif operation == '//':
            result = num1 // num2
        else:
            result = str(round(num1 / num2, 2)) + '%'
elif operation == '**':
    result = pow(num1, num2)
else:
    flag = False

    print('Invalid operation. Use "+", "-", "*", "/", "//", "%" or "**"')

if flag:
    print('Result:', result)
