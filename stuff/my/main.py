import random

""" The game random!!!"""


def is_valid(n, check_border=False):
    if not n.isdigit():
        return False
    if check_border == False and int(n) < 1 or int(b) > 100:
        return False
    if check_border == True and int(n) < 2:
        return False

    return True


def get_right_border():
    while True:
        right_border = input("Введите правую границу для отрезка чисел: ")

        if not is_valid(right_border, check_border=True):
            print(
                "Неправвильное значение границы. Граница должна быть целым положительным числом > 1"
            )
        else:
            return int(right_border)


def game():
    print("Добро пожаловать в числовую угадайку")

    right_border = get_right_border()
    N = random.randint(1, right_border)
    attemption_counter = 0

    while True:
        a = input(f"Введите число от 1 до {right_border}: ")

        if not is_valid(a) or int(a) < N or int(a) > N:
            attemption_counter += 1

        if not is_valid(a):
            print(f"А может быть все-таки введем целое число от 1 до {right_border}?")
            continue

        a = int(a)

        if a < N:
            print("Ваше число меньше загаданного, попробуйте еще разок")

            continue
        elif a > N:
            print("Ваше число больше загаданного, попробуйте еще разок")

            continue
        else:
            print(f"Вы угадали, поздравляем! Количество попыток: {attemption_counter}")
            flag = input("Сыграем ещё раз? (да/нет)")

            if flag != "да" and flag != "нет":
                print("Неправильный формат ответа")

                break
            elif flag == "нет":
                print("Очень жаль!")

                break
            else:
                print("Погнали!!!")

                right_border = get_right_border()
                N = random.randint(1, 100)
                attemption_counter = 0

                continue

    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


game()
