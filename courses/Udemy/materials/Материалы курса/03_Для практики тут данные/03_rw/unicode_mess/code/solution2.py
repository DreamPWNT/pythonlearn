# # Мое решение 2:
import os


path = os.path.dirname(os.path.dirname(__file__))  # Директория unicode_mess

destination = os.path.join(path, "new_files")  # Куда писать новые файлы.
if not os.path.exists(destination):
    os.mkdir(destination)

# Список с вариантами специально сделан в порядке убывания длины
# BOM меток, чтоб случайно не перепутать методом startswith
# b"\xff\xfe" и b"\xff\xfe\x00\x00"
encodings = [
    ["utf-32-be", b"\x00\x00\xfe\xff",],
    ["utf-32-le", b"\xff\xfe\x00\x00",],
    ["utf-8",     b"\xef\xbb\xbf",],  #это вариант "utf-8-sig"
    ["utf-16-be", b"\xfe\xff",],
    ["utf-16-le", b"\xff\xfe",],
    ["utf-8",     b"",],
]

for name in os.scandir(path):
    if not name.is_file():  # Отсеиваю имена не файлы.
        continue

    file = open(os.path.join(path, name.name), "rb")

    for encoding in encodings:
        # Для начала читаем только байты по длине предполагаемой метки.
        raw_start = file.read(len(encoding[1]))

        if raw_start == encoding[1]:

            # Пишу то что осталось уже зная кодировку.
            new_file = open(os.path.join(destination, name.name), "wb")
            # Читаем остальное (каретка чтения "помнит" откуда продолжать).
            raw_other = file.read()
            # Пишем остальное.
            new_file.write(raw_other.decode(encoding[0]).encode("utf-8"))
            new_file.close()
            break
        file.seek(0)  # Перемещаю каретку чтения в начало файла.
    file.close()