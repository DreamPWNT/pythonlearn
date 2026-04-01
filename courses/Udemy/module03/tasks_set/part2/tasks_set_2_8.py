text = input("Введите строку: ")

if len(text) > 0:
    print(f'First symbo: {text[0]}, last symbol:{text[-1]}')
else:
    print("Empty string!")
