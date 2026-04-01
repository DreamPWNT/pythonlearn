text = input("Введите строку: ")

if len(text) > 10:
    print(text[0], text[-1])
else:
    print("String is too small!")
