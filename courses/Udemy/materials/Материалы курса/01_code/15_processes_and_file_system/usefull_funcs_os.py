import os
path, path1, path2, src, dst, new_part = None   # это просто чтоб не ругалось на отсутствие переменной.

# Переменные path, path1, path2, src, dst это
# просто путь к чему то в виде строки (файлу и папке), например:
# /home/pyhs/Рабочий стол/for_tests
# C:\Users\pyhs\desktop\for_tests
# /home/pyhs/Рабочий стол/for_tests/file.txt
# C:\Users\pyhs\desktop\for_tests\file.txt

# Создание, удаление, переход
os.mkdir(path)  # создать одну директорию
os.makedirs(path)  # создать директорию и все промежуточные
os.rmdir(path)  # удалить пустую директорию
os.removedirs(path)  # удалить директорию и все пустые (если пустые) родительские
os.getcwd()  # получить текущую рабочую директорию процесса (нашего)
os.chdir(path)  # сменить текущую рабочую директорию процесса (нашего)
# Список файлов и каталогов
os.listdir(path)  # список содержимого директории
os.scandir(path)  # итерируемый объект с метаданными (эффективнее чем listdir)
os.walk(path)  # генератор обхода дерева директорий
#Удаление и перемещение файлов
os.remove(path)  # удалить файл
os.rename(src, dst)  # переименовать файл или переместить
os.replace(src, dst)  # как rename, но перезаписывает
os.unlink(path)  # синоним remove (удаление файла) только для ссылки

#os.path — работа с путями
# Объединение и получение компонентов
os.path.join(path, new_part)  # объединить части пути
os.path.basename(path)  # получить имя файла/папки без полного пути
os.path.dirname(path)  # путь к директории в котрой лежит файл или папка к которой ведет path
os.path.split(path)  # кортеж (dirname, basename)
os.path.splitext(path)  # кортеж (name, расширение файла)
#Проверка существования и типа
os.path.exists(path)  # существует ли путь
os.path.isfile(path)  # является ли файлом
os.path.isdir(path)  # является ли директорией
os.path.islink(path)  # является ли симлинком
#Прочее
os.path.getsize(path)  # размер файла в байтах
os.path.abspath(path)  # генерирует абсолютный путь из относительного
os.path.normpath(path)  # нормализованный путь (просто убирает .., .)
os.path.realpath(path)  # получить реальный путь (с учётом симлинков)
os.path.samefile(path1, path2)  # указывают ли два пути на один и тот же файл