# file = open("exceptions.markdown", "r", encoding="cp1251")

# try:
#     text = file.read()
# except UnicodeDecodeError:
#     file.reconfigure(encoding="utf-8")
#     file.seek(0)
#     text = file.read()


# print(text)



def get1():
    while True:
        try:
            num1 = float(input("1-е число: "))
            break
        except ValueError:
            print("Введите число!")
    return num1

def get_op():
    while True:
        operator = input("Оператор: ")

        if operator in ["+", "-", "*", "/"]:
            break
        print('Только "+", "-", "*", "/"')
    return operator

def get2():
    while True:
        try:
            num2 = float(input("2-е число: "))
            break
        except ValueError:
            print("Введите число!")
    return num2


def main():
    num_1 = get1()
    operator = get_op()
    num_2 = get2()

    if operator == "/":
        while True:
            try:
                result = num_1 / num_2
                break
            except ZeroDivisionError:
                print("Делить на ноль нельзя!")
                num_2 = get2()
    
    return result

print(main())