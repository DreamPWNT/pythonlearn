path = "/home/pyhs/Рабочий стол/Материалы курса/03_Для практики тут данные/03_rw/captions.sbv"
dest = "captions.txt"
file = open(path, "r", encoding="utf-8")
newf = open(dest, "w", encoding="utf-8")


for line in file:
    line = line.strip()
    if not line:
        continue
    if line.count(":") >= 4 and "," in line:
        continue
    if line.startswith("[") and line.endswith("]"):
        continue
    newf.write(line + " ")

file.close()
newf.close()