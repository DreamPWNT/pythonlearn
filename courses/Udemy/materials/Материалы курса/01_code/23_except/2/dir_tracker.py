"""Этот модуль делает "снимок" директоии (ее дерева).
Фиксирует любые изменения в файлах с момента прошлой проверки:
- файлы которые были удалены;
- файлы которые были добавлены;
- файлы (любые) у которых изменилось содержимое, хоть на "малютку байтик";

Вывод информации в терминал о всех таких файлах в формате:
 - Полный путь если walk работала от полного пути:
[+] Новый файл: /home/pyhs/course/app.py
[+] Новый файл: /home/pyhs/course/exceptions.markdown
[-] Удален файл: /home/pyhs/Рабочий стол/documents/passport.pdf
[~] Изменен файл: /home/pyhs/Рабочий стол/documents/contacts.xlsx
[~] Изменен файл: /home/pyhs/Рабочий стол/documents/passwords.docx

 - Или относительный путь если walk работала от относитеоного пути ".":
[+] Новый файл: ./course/app.py
[+] Новый файл: ./course/exceptions.markdown
[-] Удален файл: ./Рабочий стол/documents/passport.pdf
[~] Изменен файл: ./Рабочий стол/documents/contacts.xlsx
[~] Изменен файл: ./Рабочий стол/documents/passwords.docx
"""
import os
import pickle
import hashlib


# Файл pickle (SNAPSHOT - снимок/отпечаток)
SNAPSHOT_FILE = "snapshot.pkl"


def hash_file(path):
    """Возвращает хеш содержимого файла."""
    # md5 хеш мы проходили, вспоминаем.
    file =  open(path, "rb")
    file_hash = hashlib.md5(file.read()).hexdigest()
    file.close()
    return file_hash


def snapshot(directory):
    """Создает слепок (словарь) состояния каталога: имя > хеш"""
    data = {}
    # data - словарь всех файлов в каталоге и подкаталогах.
    # Ключ - путь к файлу, значение - хеш содержимого.
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)

            data[path] = hash_file(path)

    return data


def load_snapshot():
    """Загружает сохранённый слепок, если есть."""
    if os.path.exists(SNAPSHOT_FILE):
        file =  open(SNAPSHOT_FILE, "rb")
        data = pickle.load(file)
        file.close()
        return data  # dict из pickle файла
    return {}


def save_snapshot(new):
    """Сохраняем новое состояние."""
    file = open(SNAPSHOT_FILE, "wb")
    pickle.dump(new, file)
    file.close()


def watch(directory="."):
    """Сравнивает текущее состояние каталога с сохранённым."""

    print(f"Проверяем каталог: {os.path.abspath(directory)}")
    old = load_snapshot()  # Грузим словарь (старый снимок) из pkl.
    new = snapshot(directory) # Делаем новый словарь снимок.

    if not old:
        save_snapshot(new)
        print("Первый снимок сделан! Повторный запуск отобразит изменения.")
        return

    added = new.keys() - old.keys()
    removed = old.keys() - new.keys()
    changed = set()
    for f in new.keys():
        if f in old.keys() and new[f] != old[f]:
            changed.add(f)

    if not (added or removed or changed):
        print("✅ Изменений нет.")
    else:
        for f in added:
            # Не цветная Скобка [, цветной символ, опять скобка не цветная], пробел, цветной текст.
            # Напоминаю что выглядит так:  \033[1;32mТекст\033[0m
            print(f"[\033[1;32m+\033[0m] \033[1;32mНовый файл: {f}\033[0m")
        for f in removed:
            print(f"[\033[1;31m-\033[0m] \033[1;31mУдалён файл: {f}\033[0m")
        for f in changed:
            print(f"[\033[1;33m~\033[0m] \033[1;33mИзменён файл: {f}\033[0m")

    # Сохраняем новое состояние
    save_snapshot(new)


if __name__ == "__main__":
    watch(".")  # Так просто для walk указать текущую рабочую директорию (cwd)
                # Или указать /home/pyhs/Рабочий стол/, то есть полный путь.
