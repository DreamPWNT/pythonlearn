import subprocess
import time
import os

query = input("Что ищем?\n>> ")

prompt = """Введите сколько часов назад был создан файл (примерно),
или пустой ввод если любой временной промежуток.
>> """

time_stamp = int(input(prompt) or 0) * 3600
time_now = time.time()
path = "/"
matches = []

for address, dirs, files in os.walk(path):

    for file in files:
        if query in file:
            full_path = os.path.join(address, file)

            if os.path.islink(full_path):
                continue

            if time_stamp:
                if time_now - os.path.getctime(full_path) < time_stamp:
                    matches.append(full_path)

            else:
                matches.append(full_path)



if not matches:
    print("Файл не найден.")

elif len(matches) == 1:
    print("Запускаем:", matches[0])
    subprocess.run(["xdg-open", matches[0]])
    subprocess.run(f'start "" "{matches[0]}"', shell=True)

else:
    print("Найдено несколько файлов:")
    count = 0
    for i in matches:
        print(f"{count}: {i}")
        count += 1
    
    print("Выберите номер файла для запуска:")
    choice = int(input().strip())
    
    if 0 <= choice < len(matches):
        print("Запускаем:", matches[choice])
        subprocess.run(["xdg-open", matches[choice]])
        subprocess.run(f'start "" "{matches[choice]}"', shell=True)

    else:
        print("Некорректный выбор.")
