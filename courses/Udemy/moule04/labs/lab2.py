while True:
    text = input('Enter text: ')

    if text == 'q':
        print('Bye')

        break

    words_quantity = 1  # Если что-от ввели и не 'q', значит хотя бы 1 слово есть
    text_length = len(text)
    index = 0

    while index < text_length:
        if text[index] == ' ':
            words_quantity += 1

        index += 1

    print(f'Your text consists {words_quantity} words')
