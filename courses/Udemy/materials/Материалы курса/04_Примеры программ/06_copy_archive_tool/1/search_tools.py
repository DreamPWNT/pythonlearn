import os

# ! Top-Down func definitions
# Тут сейчас будем переделывать.
def simple_search(path, query, time_stamp=None, time_now=None):
    matches = []

    for address, dirs, files in os.walk(path):
        for file in files:
            if query in file:
                full_path = os.path.join(address, file)  # Формируем полный путь к файлу

                if os.path.islink(full_path):  # Если симлинк пропускаем
                    continue

                if time_stamp:  # Если есть временной диапазон проаеряем
                    if time_now - os.path.getctime(full_path) < time_stamp:
                        matches.append(full_path)

                else:           # Без временного диапазона сразу добавляем в список совпадений
                    matches.append(full_path)
    return matches