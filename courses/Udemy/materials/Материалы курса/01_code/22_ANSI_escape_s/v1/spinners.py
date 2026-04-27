import time, os

os.system("")

for i in range(101):
    print(f"\rЗагрузка: {i}%", end="", flush=True)
    time.sleep(0.05)

print("\nГотово!")
##############################################################################
for i in range(101):
    color = "\033[92m" if i < 100 else "\033[91m"
    print(f"\r{color}Прогресс: {i}%\033[0m", end="", flush=True)
    time.sleep(0.05)

print("\nГотово!")
###############################################################################
import time

def progress_bar(percent, width=30):
    filled = int(width * percent // 100)
    bar = '█' * filled + '░' * (width - filled)
    print(f"\rЗагрузка: |{bar}| {percent:3d}%", end='', flush=True)

for i in range(101):
    progress_bar(i)
    time.sleep(0.05)

print("\nГотово!")
###############################################################################
import time
import itertools

spinner = itertools.cycle('|/-\\')  # бесконечный цикл по символам

for i in range(100):
    sym = next(spinner)
    print(f"\rОжидание... {sym}", end='', flush=True)
    time.sleep(0.1)

print("\nГотово!")
###############################################################################
import time
import itertools

spinner = itertools.cycle('|/-\\')  # бесконечный цикл по символам
spinner2 = itertools.cycle("🤭"*8+"😜"*8+"🤫"*8+"🤔")  # слишком быстро, нужны дубли
width = 30

    

for percent in range(101):
    filled = int(width * percent // 100)
    sym = next(spinner)

    bar = '█' * filled + '░' * (width - filled)
    print(f"\rЗагрузка: |{bar}| {sym} {percent:3d}%", end='', flush=True)
    time.sleep(0.05)



print("\nГотово!")
