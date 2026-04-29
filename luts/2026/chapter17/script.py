import scopes101
import builtins
import thismod

print(scopes101.func(1))
print(dir(builtins))
print(len(dir(builtins)), len(
    [x for x in dir(builtins) if not x.startswith('__')]))

X = 88


def func():
    global X

    X = 99


func()

print(X)

y, z = 1, 2


def all_global():
    global x

    x = y + z


print(thismod.test())
print(thismod.var)
