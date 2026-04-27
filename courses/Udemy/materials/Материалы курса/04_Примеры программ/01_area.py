import math

print("Программа калькулятор площади фигур")
print('Введите:\n"s" - для квадрата\n"r" - для прямоугольника\n"c" - для круга')

choice = input("Ваш выбор: ")

if choice == "s":
    side = float(input("Введите длину стороны квадрата: "))
    area = side**2
    print("Площадь квадрата: " + str(area))

elif choice == "r":
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    area = length * width
    print("Площадь прямоугольника: " + str(area))

elif choice == "c":
    radius = float(input("Введите радиус круга: "))
    area = math.pi * radius**2
    print("Площадь круга: " + str(area))

else:
    print("Ошибка: неверный ввод, попробуйте снова.")
