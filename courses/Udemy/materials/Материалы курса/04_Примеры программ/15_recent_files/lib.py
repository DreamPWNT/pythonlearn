import os
import sys
import time

from exclude import exclude_names


def recent_files(path, time_stamp):
    time_now = time.time()
    for address, dirs, files in os.walk(path):
        exclude_name(dirs)
        exclude_name(files)

        for file in files:
            full_path = os.path.join(address, file)
            if os.path.islink(full_path):
                continue
            if time_now - os.path.getctime(full_path) < time_stamp:
                print(full_path)


def exclude_name(paths: list[str]):
    for name in exclude_names:
        for i in range(len(paths) - 1, -1, -1):
            if name in paths[i].lower():
                paths.pop(i)


def get_user_space() -> list[str]:
    """Возвращает список файлового пространства пользователя:
        - директория пользователя в системном диске;
        - остальные доступные дисковые пространства общего пользования.

    Returns:
        list[str]: список путей
    """
    spaces = []

    if sys.platform.startswith("win"):
        # Домашняя папка
        home_dir = os.path.expanduser("~")
        spaces.append(home_dir)

        # Все доступные диски (C:, D:, ...)
        # os.listdrives() появилась в python3.12 для windows.
        # В версих старее нужно было делать итерацию по алфавиту в верхнем регистре
        # и проверять через os.path.exists каждую букву D:\\ и тд.
        drives = os.listdrives()[1:]
        spaces.extend(drives)

    elif sys.platform.startswith("darwin"):
        # Домашняя папка
        home_dir = os.path.expanduser("~")
        spaces.append(home_dir)

        # Общие точки монтирования
        volumes_dir = "/Volumes"
        if os.path.exists(volumes_dir):
            for item in os.listdir(volumes_dir):
                spaces.append(os.path.join(volumes_dir, item))

    elif sys.platform.startswith("linux"):
        # Домашняя папка
        home_dir = os.path.expanduser("~")
        spaces.append(home_dir)

        # Общие точки монтирования
        for mount_dir in ("/media", "/mnt"):
            if os.path.exists(mount_dir):
                for item in os.listdir(mount_dir):
                    spaces.append(os.path.join(mount_dir, item))

    else:
        print("Неизвестная платформа")
        exit(1)

    return spaces


if __name__ == "__main__":
    for path in get_user_space():
        print(path)  # тест-проверка пользовательских директорий и томов(дисков)
