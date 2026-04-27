"""P.S. Для Mac нет Mac чтоб проверить, поэтому первопроходцы напишите работает или нет,
исправлю.
"""

import os
import subprocess
import sys
import time


is_windows = sys.platform.startswith("win")
is_linux = sys.platform.startswith("linux")
is_mac = sys.platform.startswith("darwin")

if is_windows:
    clear_command = "cls"
    os.system("chcp 866") # чтоб знать в какой колировке будет от dir вывод точно, она ее возьмет
    # Команда для проверки свободного места
    # Windows: используем команду "dir" для основного диска (C:)
    command = ["cmd", "/c", "dir C:"]
    # "dir" в Windows выводит информацию о содержимом диска.
    # В конце вывода указывается количество свободных байт, например:
    # "X Dir(s)  Y bytes free".
    # Мы будем парсить последнюю строку вывода.
    disk_name = "C:"
elif is_mac:
    clear_command = "clear"
    # Команда для проверки свободного места
    # Mac: используем команду "df" для корневого раздела (/)
    command = ["zsh", "-c", "df -h /"]
    # Аналогично Linux, "df -h /" выводит информацию о диске в человекочитаемом формате.
    # Вывод похож на Linux, нас интересует колонка "Avail".
    disk_name = "/"
elif is_linux:
    clear_command = "clear"
    # Команда для проверки свободного места
    # Linux: используем команду "df" для корневого раздела (/)
    command = ["bash", "-c", "df -h /"]
    # "df" выводит информацию о дисковом пространстве.
    # -h — в человекочитаемом формате (например, GB вместо байтов).
    # "/" — корневой раздел, основной диск в большинстве систем.
    # Вывод: "Filesystem Size Used Avail Use% Mounted on".
    # Нас интересует колонка "Avail" (доступно).
    disk_name = "/"
else:
    print("❌ Неизвестная ОС. Поддерживаются: Linux, macOS, Windows.")


simple_loader = "|" * 38

os.system(clear_command)

print("💾 Проверка свободного места на диске...")
# В этой программе это только для важности, вроде мы что-то меряем...
for i in simple_loader:
    print(i, end="", flush=True)  # print без end='\n' буферизируется (лоадер не получится)
    time.sleep(2/len(simple_loader))
else:
    print("✔️")


if is_windows:
    # Для Windows: берём последнюю строку из вывода "dir"
    result = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding="cp866")
    output = result.communicate()[0].strip()
    lines = output.splitlines()
    last_line = lines[-1].strip()
    # Пример: "18 папок  156 655 710 208 байт свободно" и разбираем это, забирая нужное:
    free_space = last_line.split()[2:-2]
    free_space = round(int("".join(free_space))/(1024**3))
    print(f"📂 Диск {disk_name} свободно {free_space} Gb")
elif is_linux or is_mac:
    result = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    output = result.communicate()[0].strip()
    # Для Linux/Mac: берём вторую строку из вывода "df -h"
    lines = output.splitlines()
    data_line = lines[1].strip()
    # Пример: "/dev/disk1s1  477Gi  400Gi  77Gi  84%  /"
    free_space = data_line.split()[3]  # Колонка 4
    used_space = data_line.split()[4]  # Колонка 5
    print(f"📂 Диск {disk_name}: свободно {free_space} ; использовано {used_space}")
