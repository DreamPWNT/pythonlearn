import shutil

# Копирование файла
shutil.copy("/home/pyhs/Рабочий стол/process.png", "/home/pyhs/Рабочий стол/process(2).png")
shutil.copy("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")


# Копирование файла с сохранением всех метаданных (для резервных копий хорошо)
shutil.copy2("/home/pyhs/Рабочий стол/docs/one.txt", "/home/pyhs/Рабочий стол/test/")
shutil.copy2("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")


# Копирование директории (без символических ссылок)
shutil.copytree("/home/pyhs/Рабочий стол/docs", "/home/pyhs/Рабочий стол/test/", dirs_exist_ok=True)
shutil.copytree("C:/Users/PyHS/Desktop/docs", "C:/Users/PyHS/Desktop/test/", dirs_exist_ok=True)


# Перемещение файла
shutil.move("/home/pyhs/Рабочий стол/docs/one.txt", "/home/pyhs/Рабочий стол/test/")  # Файл в сущ. директорию
shutil.move("/home/pyhs/Рабочий стол/docs", "/home/pyhs/Рабочий стол/test/")  # Дир. в сущ. директорию
shutil.move("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")
shutil.move("C:/Users/PyHS/Desktop/docs", "C:/Users/PyHS/Desktop/test/")


# Удаление директории
shutil.rmtree("/home/pyhs/Рабочий стол/docs")
shutil.rmtree("C:/Users/PyHS/Desktop/docs")


# Создание архива
# Первый аргумент - куда и имя архива без расширения, третий аргумент - что архивировать
shutil.make_archive("/home/pyhs/Рабочий стол/docs_backup", 'zip', "/home/pyhs/Рабочий стол/docs")
shutil.make_archive("/home/pyhs/Рабочий стол/docs_backup", 'gztar', "/home/pyhs/Рабочий стол/docs")
shutil.make_archive("C:/Users/PyHS/Desktop/docs_backup", 'zip', "C:/Users/PyHS/Desktop/docs")


# Распаковка архива
# unpack_archive - автоматически определяет тип архива по расширению
shutil.unpack_archive("/home/pyhs/Рабочий стол/docs_backup.zip", "/home/pyhs/Рабочий стол/")
shutil.unpack_archive("C:/Users/PyHS/Desktop/docs_backup.zip", "C:/Users/PyHS/Desktop/")

