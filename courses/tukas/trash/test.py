import os
import sys


print("Автоматический запуск программ.")

if sys.platform.startswith("win"):
    os.system("start https://www.google.com")
    os.system("start notepad")
    # os.startfile("notepad")

elif sys.platform.startswith("darwin"):
    os.system("open https://www.google.com")
    os.system("open -a TextEdit")

elif sys.platform.startswith("linux"):
    os.system("bash -c 'xdg-open https://www.google.com & disown'")
    os.system("bash -c 'gedit & disown'")

else:
    print("Эта ОС не предусмотрена.")

print("Программа завершена (Код Python отработал).")
