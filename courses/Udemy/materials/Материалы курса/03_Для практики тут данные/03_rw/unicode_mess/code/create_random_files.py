# Для начала генерация файлов с рандомным выбором кодировки.
import random
import os


path = os.path.dirname(os.path.dirname(__file__))  # Директория unicode_mess

text = "Текст для записи in file в\nразных encodings а также\ndifferent byte order маркировкой xD)))))."

encodings = [  # Кодировка - BOM метка.
    ["utf-8",     b"",],
    ["utf-8-sig", b"\xef\xbb\xbf",],
    ["utf-16-le", b"\xff\xfe",],
    ["utf-16-be", b"\xfe\xff",],
    ["utf-32-le", b"\xff\xfe\x00\x00",],
    ["utf-32-be", b"\x00\x00\xfe\xff",],
]

for i in range(10):  # Десять файлов.
    file = open(os.path.join(path, f"{i}.txt"), "wb")
    choice = random.choice(encodings)  # Случайная кодировка.

    new_text = text + f"\nЭтот файл был в {choice[0]}"  

    file.write(choice[1])  # Запись в файл метки BOM
    if choice[0] == "utf-8-sig":  # BOM для utf-8-sig уже был записан в файл, и
        encoding = "utf-8"        # чтоб метод encode (ниже) недбавил второй раз BOM.
    else:
        encoding = choice[0]
    file.write(new_text.encode(encoding=encoding))
    file.close()
