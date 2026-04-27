import shutil

# Копирование файла
# Linux (bash): cp /home/pyhs/Рабочий\ стол/docs/one.txt /home/pyhs/Рабочий\ стол/test/
# Mac (zsh): cp /home/user/Рабочий\ стол/docs/text.txt /home/user/Рабочий\ стол/test/
# Windows (PowerShell): Copy-Item -Path C:\Users\PyHS\Desktop\docs\text.txt -Destination C:\Users\PyHS\Desktop\test\

# shutil.copy("/home/pyhs/Рабочий стол/docs/one.txt", "/home/pyhs/Рабочий стол/test/")
# shutil.copy("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")


# Копирование файла с сохранением всех метаданных (для резервных копий хорошо)
# Linux (bash): cp --preserve=all /home/pyhs/Рабочий\ стол/docs/one.txt /home/pyhs/Рабочий\ стол/test/
# Mac (zsh): cp -p /home/user/Рабочий\ стол/docs/text.txt /home/user/Рабочий\ стол/test/
# Windows (PowerShell): Copy-Item -Path C:\Users\PyHS\Desktop\docs\one.txt -Destination C:\Users\PyHS\Desktop\test\ -Force

# shutil.copy2("/home/pyhs/Рабочий стол/docs/one.txt", "/home/pyhs/Рабочий стол/test/")
# shutil.copy2("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")


# Копирование директории (без символических ссылок)
# Linux (bash): cp -r /home/pyhs/Рабочий\ стол/docs /home/pyhs/Рабочий\ стол/test/
# Mac (zsh): cp -R /home/user/Рабочий\ стол/docs /home/user/Рабочий\ стол/test/
# Windows (PowerShell): Copy-Item -Path C:\Users\PyHS\Desktop\docs -Destination C:\Users\PyHS\Desktop\test\ -Recurse

# shutil.copytree("/home/pyhs/Рабочий стол/docs", "/home/pyhs/Рабочий стол/test/", dirs_exist_ok=True)
# shutil.copytree("C:/Users/PyHS/Desktop/docs", "C:/Users/PyHS/Desktop/test/", dirs_exist_ok=True)


# Перемещение файла
# Linux (bash): mv /home/pyhs/Рабочий\ стол/docs/text.txt /home/pyhs/Рабочий\ стол/test/
# Mac (zsh): mv /home/user/Рабочий\ стол/docs/text.txt /home/user/Рабочий\ стол/test/
# Windows (PowerShell): Move-Item -Path C:\Users\PyHS\Desktop\docs\text.txt -Destination C:\Users\PyHS\Desktop\test\

# shutil.move("/home/pyhs/Рабочий стол/docs/one.txt", "/home/pyhs/Рабочий стол/test/")  # Файл в сущ. директорию
# shutil.move("/home/pyhs/Рабочий стол/docs", "/home/pyhs/Рабочий стол/test/")  # Дир. в сущ. директорию
# shutil.move("C:/Users/PyHS/Desktop/docs/one.txt", "C:/Users/PyHS/Desktop/test/")
# shutil.move("C:/Users/PyHS/Desktop/docs", "C:/Users/PyHS/Desktop/test/")


# Удаление файла
# Linux (bash): rm /home/pyhs/Рабочий\ стол/docs/text.txt
# Mac (zsh): rm /home/user/Рабочий\ стол/docs/text.txt
# Windows (PowerShell): Remove-Item -Path C:\Users\PyHS\Desktop\docs\text.txt -Force

# os.remove("/home/pyhs/Рабочий стол/docs/two.txt")
# os.remove("C:/Users/PyHS/Desktop/docs/text.txt")


# Удаление директории
# Linux (bash): rm -r /home/pyhs/Рабочий\ стол/docs/
# Mac (zsh): rm -R /home/user/Рабочий\ стол/docs/
# Windows (PowerShell): Remove-Item -Path C:\Users\PyHS\Desktop\docs -Recurse -Force

# shutil.rmtree("/home/pyhs/Рабочий стол/docs")
# shutil.rmtree("C:/Users/PyHS/Desktop/docs")


# Создание директории
# Linux (bash): mkdir -p /home/pyhs/Рабочий\ стол/test_folder
# Mac (zsh): mkdir -p /home/user/Рабочий\ стол/test_folder
# Windows (PowerShell): New-Item -Path C:\Users\PyHS\Desktop\test_folder -ItemType Directory

# os.makedirs("/home/pyhs/Рабочий стол/test_folder", exist_ok=True)
# os.makedirs("C:/Users/PyHS/Desktop/test_folder", exist_ok=True)


# Создание архива
# Linux (bash) / Mac (zsh):
# tar -czf /home/pyhs/Рабочий\ стол/docs_backup.tar.gz /home/pyhs/Рабочий\ стол/docs
# zip -r /home/pyhs/Рабочий\ стол/docs_backup.zip /home/pyhs/Рабочий\ стол/docs
# Windows (PowerShell):
# Compress-Archive -Path C:\Users\PyHS\Desktop\docs -DestinationPath C:\Users\PyHS\Desktop\docs_backup.zip

# Первый аргумент - куда и имя архива без расширения, третий аргумент - что архивировать
# shutil.make_archive("/home/pyhs/Рабочий стол/docs_backup", 'zip', "/home/pyhs/Рабочий стол/docs")
# shutil.make_archive("/home/pyhs/Рабочий стол/docs_backup", 'gztar', "/home/pyhs/Рабочий стол/docs")
# shutil.make_archive("C:/Users/PyHS/Desktop/docs_backup", 'zip', "C:/Users/PyHS/Desktop/docs")


# Распаковка архива
# Linux (bash) / Mac (zsh):
# tar -xzf /home/pyhs/Рабочий\ стол/docs_backup.tar.gz -C /home/pyhs/Рабочий\ стол/
# unzip /home/pyhs/Рабочий\ стол/docs_backup.zip -d /home/pyhs/Рабочий\ стол/
# Windows (PowerShell):
# Expand-Archive -Path C:\Users\PyHS\Desktop\docs_backup.zip -DestinationPath C:\Users\PyHS\Desktop\docs

# unpack_archive - автоматически определяет тип архива по расширению
# shutil.unpack_archive("/home/pyhs/Рабочий стол/docs_backup.zip", "/home/pyhs/Рабочий стол/")
# shutil.unpack_archive("C:/Users/PyHS/Desktop/docs_backup.zip", "C:/Users/PyHS/Desktop/")

