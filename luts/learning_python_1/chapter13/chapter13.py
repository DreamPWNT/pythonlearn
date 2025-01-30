import os

x = "spam"

while x:
    print(x, end=" ")
    x = x[1:]

print()

a = 0
b = 10

while a < b:
    print(a, end=" ")
    a += 1

print()

x = 10

while x:
    x = x - 1

    if x % 2 != 0:
        continue

    print(x, end=" ")
"""
while True:
    name = input("Enter name (print 'stop' to exit): ")

    if name == "stop":
        break
    age = input("Enter age:")
    print("Hello", name, "=>", int(age) ** 2)
"""
y = 11
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, "has factor", x)

        break

    x -= 1
else:
    print(y, "is prime")

for x in ["spam", "eggs", "ham"]:
    print(x, end=" ")

sum = 0
prod = 1

for x in [1, 2, 3, 4]:
    sum += x
    prod *= x

print(sum, prod)

S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S:
    print(x, end=" ")

for x in T:
    print(x, end=" ")

print()

T = [(1, 2), (3, 4), (5, 6)]

for a, b in T:
    print(a, b)

D = {"a": 1, "b": 2, "c": 3}

for key in D:
    print(key, "=>", D[key])

print(list(D.items()))

for key, value in D.items():
    print(key, "=>", value)

for both in T:
    a, b = both
    print(a, b)

for (a, b), c in ((1, 2), 3), ["XY", 6]:
    print(a, b, c)

items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found")

seq1 = "spam"
seq2 = "scam"
res = []

for item in seq1:
    if item in seq2:
        res.append(item)

print(res)

res = [x for x in seq1 if x in seq2]

print(res)

print(
    list(range(5)),
    list(range(2, 5)),
    list(range(0, 10, 2)),
    list(range(-5, 5)),
    list(range(5, -5, -1)),
)

for i in range(3):
    print(i, "Pythons")

X = "spam"

for item in X:
    print(item, end=" ")

i = 0

while i < len(X):
    print(X[i], end=" ")
    i += 1

print()

S = "spam"

for i in range(len(S)):
    S = S[1:] + S[:1]

    print(S, end=" ")

print()

for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end=" ")

print()

L = [1, 2, 3]

for i in range(len(L)):
    X = L[i:] + L[:i]

    print(X, end=" ")

print()

S = "abcdefghijk"

print(list(range(0, len(S), 2)))

for i in list(range(0, len(S), 2)):
    print(S[i], end=" ")

print()

for c in S[::2]:
    print(c, end=" ")

print()

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 1

print(L)

i = 0

while i < len(L):
    L[i] += 1
    i += 1

print(L)

print([x + 1 for x in L])

L1 = [1, 2, 3, 4, 10, 333, 444]
L2 = [5, 6, 7, 8, 9, 111]

print(list(zip(L1, L2)))

for x, y in zip(L1, L2):
    print(x, y, "++++", x + y, "----", x - y, "****", x * y, "////", x / y)

print(list(map(ord, "spam")))

keys = ["spam", "eggs", "toast"]
vals = [1, 3, 5]

print(list(zip(keys, vals)))

D2 = {}

for k, v in zip(keys, vals):
    D2[k] = v

print(D2)

D3 = dict(zip(keys, vals))

print(D3)

print({k: v for (k, v) in zip(keys, vals)})

S = "spam"

for idx, item in enumerate(S):
    print(item, "appears at offset", idx)

E = enumerate(S)

print(E)
print(next(E))
print(next(E))
print(next(E))
print(next(E))

F = os.popen("dir")

print(repr(F.readline()))

F = os.popen("dir")

print(repr(F.readline(50)))

print(os.popen("dir").readlines())


for line in os.popen("dir"):
    print(line.rstrip())

print(os.system("systeminfo"))

for line in os.popen("systeminfo"):
    print(line.rstrip())

for i, line in enumerate(os.popen("systeminfo")):
    if i == 4:
        break
    print("%05d) %s" % (i, line.rstrip()))
