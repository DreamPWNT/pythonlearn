name = input("Введите Имя: ")
last_name = input("Введите Фамилию: ")

if ' ' in name or ' ' in last_name:
    print('Attention to fill form! It was last blank muhahahahahah!!!!')
else:
    result = name + ' ' + last_name

    print(result)
