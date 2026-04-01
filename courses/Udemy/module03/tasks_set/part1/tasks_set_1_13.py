num = input("Введите число: ")

if '.' in num:
    num = float(num)
else:
    num = int(num)

print(num)
