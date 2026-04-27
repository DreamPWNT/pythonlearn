import os
import subprocess

# x = os.system("python3.13 myapp.py")

command = ["python3.13", "-u", "myapp.py"]

# x = subprocess.run(command)

# x = subprocess.run(command, stdout=subprocess.PIPE, text=True, encoding="utf-8")
# print(x.stdout.strip() + " Whoa!")

# x = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding="utf-8")
# stdout, stderr = x.communicate()
# print(stdout.strip() + " Whoa!")

# x = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding="utf-8")

# for item in x.stdout:
#     print(item.strip() + " Whoa!")
#     x.terminate()

# file = open("out.txt", "w", encoding="utf-8")

# x = subprocess.Popen(command, stdout=file, text=True, encoding="utf-8")

# x = os.popen("python3.13 myapp.py")
# print(x.read().strip() + " Whoa!")


print("Next code")
