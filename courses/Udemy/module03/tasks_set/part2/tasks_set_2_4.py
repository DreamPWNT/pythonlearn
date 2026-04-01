text = input("Введите сообщение: ")

if len(text) > 6 and text[-1] == '!':
    print('Emotional message!')
else:
    print('Common message')
