# Python documentation

import sys

print(dir(sys))
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.endswith("__")]))
print(len([x for x in dir(sys) if not x[0] != "_"]))
print(dir([]))
print(dir(""))
print([x for x in dir(list) if not x.startswith("__")])
print([x for x in dir(dict) if not x.startswith("__")])
print([x for x in dir(list) if not x[0] == "_"])
print([x for x in dir(dict) if not x[0] == "_"])


def dir1(x):
    return [x for x in dir(x) if not x.startswith("__")]


print(dir1(sys))

"""
Words Fo Here
"""

spam = 40


def square(x):
    """
    Function squared int

    Args:
        x (int or float): return squared value
    """
    return x**2


class Employee:
    """
    class documentation
    """

    pass


print(square(4))
print(square.__doc__)
print(sys.__doc__)
print(sys.getrefcount.__doc__)
print(int.__doc__)
print(map.__doc__)
print(help(sys.getrefcount))
print(help(str.replace))
print(help("".replace))
print(help(ord))

S = "vodochka i seledochka"
L_ord = []

sum = 0
for ch in S:
    sum += ord(ch)
    L_ord.append(ord(ch))

    print(ch, "code =", ord(ch))

print("sum =", sum)
print(L_ord)

print(map(ord, S))
print([ord(ch) for ch in S])

for i in range(50):
    print("Hello %d\n\a" % i)

D = {"f": 1, "a": 34, "y": 12, "h": 545, "z": 321, "c": -9}
D_sorted = {}

L_keys = sorted(list(D.keys()))
L_keys = list(D.keys())
L_keys.sort()

for key in L_keys:
    D_sorted[key] = D[key]

    print(key, "=>", D[key])

L = [1, 2, 4, 8, 16, 32, 4]
X = 5
found = False
i = 0

while not found and i < len(L):
    if 2**X == L[i]:
        found = True
    else:
        i = i + 1

if found:
    print("at index", i)
else:
    print(X, "not found")

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

while i < len(L):
    if 2**X == L[i]:
        print("at index", i)

        break
    else:
        i = i + 1
else:
    print(X, "not found")

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

for idx in range(len(L)):
    if 2**X == L[idx]:
        print("at index", idx)

        break
else:
    print(X, "not found")

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2**X in L:
    print("at index", L.index(2**X))
else:
    print(X, "not found")

L = [2**x for x in range(0, 7)]

if 2**X in L:
    print("at index", L.index(2**X))
else:
    print(X, "not found")
