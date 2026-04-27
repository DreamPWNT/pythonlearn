import shlex

test1 = 'ls "/path/t o/anything"'

test2 = 'ls "C:\\Users\\путь\\c пробелом\\Desktop\\соответственно с кавычками\\"'
print(test2)

res = shlex.split(test1)
print(res)
res = shlex.split(test2, posix=False)
print(res)
