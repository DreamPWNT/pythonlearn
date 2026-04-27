print("Программа калькулятор")

num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неверная операция!"

print("Ответ: " + str(result))
