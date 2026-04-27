import os

path = "/home/pyhs/Рабочий стол/temp"
if not os.path.exists(path):
    os.mkdir(path)


path = "../Рабочий стол/temp"
#      /home/pyhs/course
if not os.path.exists(path):
    os.mkdir(path)
