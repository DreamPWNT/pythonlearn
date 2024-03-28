for x in [1, 2, 3, 4]:
    print(x**2, end=" ")

for x in (1, 2, 3, 4):
    print(x**3, end=" ")

for x in "spam":
    print(x * 2, end=" ")

for line in open("luts/learning_python_1/chapter5.py"):
    print(line.upper(), end="")

f = open("luts/learning_python_1/chapter5.py")

print(f.__next__())
print(f.__next__())
print(f.__next__())
print(next(f))
print(next(f))
print(next(f))

L = [1, 2, 3]
I = iter(L)

print(I)

print(I.__next__())
print(I.__next__())
print(I.__next__())

for X in L:
    print(X**2, end=" ")

I = iter(L)

while True:
    try:
        X = next(I)
    except StopIteration:
        break

    print(X**2, end=" ")

D = {"a": 1, "b": 2, "c": 3}

for key in D.keys():
    print(key, D[key])

I = iter(D)

print(next(I))
print(next(I))
print(next(I))

for key in D:
    print(key, D[key])

L = [3, 4, 3, 56, 23]

L = [x + 33 for x in L]

print(L)

lines = open("luts/learning_python_1/chapter5.py").readlines()

print(lines)

lines = [line.rstrip() for line in lines]

print(lines)

lines = [line.rstrip() for line in open("luts/learning_python_1/chapter5.py")]

print(lines)

lines = [line.split() for line in open("luts/learning_python_1/chapter5.py")]

print(lines)

lines = [
    line.rstrip()
    for line in open("luts/learning_python_1/chapter5.py")
    if line[0] == "p"
]

print()
print()
print(lines)

print([x + y for x in "abc" for y in "lmn"])

print(list(map(str.upper, open("luts/learning_python_1/chapter5.py"))))

a, b, c, *d = open("luts/learning_python_1/chapter5.py")

print(a)
print(b)
print(c)
print(d)

print('print("%e" % num)\n' in open("luts/learning_python_1/chapter5.py"))

print(max(open("luts/learning_python_1/chapter5.py")))
print(min(open("luts/learning_python_1/chapter5.py")))

print(*[1, 2, 3, 4])
print([1, 2, 3, 4])

X = (1, 2)
Y = (3, 4)

A, B = zip(*zip(X, Y))

print(A, B)

print(list(zip("abc", "xyz")))

R = range(0, 10)
print(R[4])
I = iter(R)

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

M = map(abs, (-1, 0, 1))

print(M)
print("It's iterator", next(M))
print("It's iterator", next(M))
# print(next(M))

for x in M:
    print("It's for", x)

Z = zip((1, 2, 3), (40, 50, 60))

print(Z)
print(list(Z))

for x in Z:
    print(x)

D = dict(g=8, a=2, c=3)

print(D)

K = D.keys()

print(K)

I = iter(K)

print(next(I))
print(next(I))
print(next(I))

for k in D.keys():
    print(k, end=" ")

for k in sorted(D.keys()):
    print(f"{k}: {D[k]}")
