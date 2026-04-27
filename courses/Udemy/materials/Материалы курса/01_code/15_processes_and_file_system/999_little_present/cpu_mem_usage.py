"""P.S. Для Mac нет Mac чтоб проверить, поэтому первопроходцы напишите работает или нет,
исправлю.
"""
import os
import subprocess
import sys
import time


is_windows = sys.platform.startswith("win")
is_mac = sys.platform.startswith('darwin')
is_linux = sys.platform.startswith('linux')

if is_windows:
    clear_command = "cls"

    command_1 = ["powershell", "-Command", "Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty LoadPercentage"]
    command_2 = ["powershell", "-Command", "Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object FreePhysicalMemory, TotalVisibleMemorySize"]
    # В Power Shell точно так же как и в python многое описано объектами, в том числе информация о системе.
    # Если ввести просто Get-CimInstance -ClassName Win32_Processor то нам вернется "объект" описывающий
    # процессор, а отобразится просто общая информация. Чтоб получить более глубокие данные из этого объекта,
    # передаем через | в Select-Object (выбрать объект) и указываем что нужно получить информацию из
    # свойства LoadPercentage.
    # Всю эту информацию, о том как использовать нужно просто гуглить или читать документацию
    # https://go.microsoft.com/fwlink/?LinkId=227961
elif is_mac:
    clear_command = "clear"
    command_1 = ["zsh", "-c", "top -l 1 | grep 'CPU usage'"]
    # Утилита top в Linux/Mac запущенная без параметров итак в режиме реалтайм обновляет
    # показания. Но, нам интересно получить вывод в python.
    # Команда top -l 1 используется в Mac для получения однократного
    # снимка состояния системы.
    # -l 1 показывает только один снимок состояния системы и завершает работу.
    # (Если бы было -l 5, top сделал бы 5 снимков с интервалом в несколько секунд.)
    # Расшифровка вывода:
    # user - Время, потраченное на пользовательские процессы (не ядро).
    # sys  - Время, потраченное ядром (системные вызовы, драйверы и т.п.).
    # idle - Процент времени, когда CPU простаивает.
    command_2 = ["zsh", "-c", "top -l 1 | grep PhysMem"]
elif is_linux:
    clear_command = "clear"
    command_1 = ["bash", "-c", "top -bn1 | grep '%Cpu'"]
    # Утилита top в Linux/Mac запущенная без параметров итак в режиме реалтайм обновляет
    # показания. Но, нам интересно получить вывод в python.
    # Команда top -bn1 используется в Linux для получения однократного
    # снимка состояния системы.
    # -b (batch mode)
    # Выводит top в формате, удобном для парсинга или записи в файл.
    # Не требует интерактивного режима, поэтому его можно использовать в скриптах.
    # -n1 показывает только один снимок состояния системы и завершает работу.
    # (Если бы было -n5, top сделал бы 5 снимков с интервалом в несколько секунд.).
    # Расшифровка вывода:
    # us - user         - Время, потраченное на пользовательские процессы (не ядро).
    # sy - system       - Время, потраченное ядром (системные вызовы, драйверы и т.п.).
    # ni - nice         - Время пользовательских процессов с изменённым приоритетом (nice).
    # id - idle         - Процент времени, когда CPU простаивает.
    # wa - wait         - Время ожидания ввода-вывода (например, диск или сеть "тормозит").
    # hi - hardware IRQ - Обработка аппаратных прерываний.
    # si - software IRQ - Обработка программных прерываний.
    # st - steal        - Время, "украденное" у VM гипервизором (актуально для виртуальных машин).
    command_2 = ["bash", "-c", "free -h"]
    # free выводи информацию об оперантивной памяти.
    # -h - в гигабайтах, -m - в мегабайтах
else:
    print("❌ Неизвестная ОС. Поддерживаются: Linux, macOS, Windows.")

update_time = 2
simple_loader = "|"*80
data_for_next_round = "Загрузка", "Загрузка"

while True:
    cpu_info = subprocess.Popen(command_1, stdout=subprocess.PIPE, text=True)
    mem_info = subprocess.Popen(command_2, stdout=subprocess.PIPE, text=True)

    os.system(clear_command)
        
    print("🔧 Системный монитор (CPU / Память)")
    print(simple_loader)

    if is_windows:
        print("📈 CPU: ", end="")
    else:
        print("📈 CPU:")
    print(data_for_next_round[0])
    print("🧠 Memory:")
    print(data_for_next_round[1])

    print(f"\nНажмите Ctrl+C для выхода. Обновление каждые {update_time} сек.")
        
    for i in simple_loader:
        print(i, end='', flush=True)  # print без end='\n' буферизируется (лоадер не получится)
        time.sleep(update_time/len(simple_loader))
    else:
        print()
        
    if is_windows:
        cpu = cpu_info.communicate()[0].strip() + "%"
        mem = mem_info.communicate()[0].strip()
        mem = mem.splitlines()[2].split()
        mem_available = f"Доступно {round(int(mem[0])/1024)} Mb"
        all_mem = f" из {round(int(mem[1])/1024)} Mb"
        data_for_next_round = cpu, mem_available + all_mem
    else:
        data_for_next_round = cpu_info.communicate()[0], mem_info.communicate()[0]
