import os
import functools, operator

for x in [1, 2, 3, 4]:
    print(x**2, end=" ")

for x in (1, 2, 3, 4):
    print(x**3, end=" ")

for x in "spam":
    print(x * 2, end=" ")

for line in open("luts/learning_python_1/data/chapter5.py"):
    print(line.upper(), end="")

f = open("luts/learning_python_1/data/chapter5.py")

print(f.__next__())
print(f.__next__())
print(f.__next__())

for line in open("luts/learning_python_1/data/chapter5.py"):
    print(line.upper(), end="")

print()

f = open("luts/learning_python_1/data/chapter5.py")

print(f.__next__(), end="")
print(f.__next__(), end="")

f = open("luts/learning_python_1/data/chapter5.py")

print(next(f), end="")
print(next(f), end="")

L = [1, 2, 3, 4]
I = iter(L)

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())

f = open("luts/learning_python_1/data/chapter5.py")

print(f)
print(iter(f))
print(f.__iter__())
print()
print(f.__next__())


L = [1, 2, 3, 4]

for X in L:
    print(X**2, end=" ")

print()

I = iter(L)

while True:
    try:
        X = next(I)
    except StopIteration:
        break

    print(X**2, end=" ")

print()

D = {"a": 1, "b": 2, "c": 3}

for key in D.keys():
    print(key, D[key])

I = iter(D)


print(next(I))
print(next(I))
print(next(I))

for key in D:
    print("key =>", key)

P = os.popen("dir")

print(P.__next__())
print(P.__next__())


P = os.popen("dir")
I = iter(P)

print(next(I))
print(I.__next__())

R = range(5)

print(R)

I = iter(R)

print(next(I))
print(next(I))
print(list(range(5)))

E = enumerate("spam")

print(E)

I = iter(E)

print(next(I))
print(next(I))
print(list(enumerate("spam")))

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10

print(L)

L = [x + 10 for x in L]

print(L)

f = open("luts/learning_python_1/data/chapter5.py")

lines = f.readlines()

print(lines)

lines = [line.rstrip() for line in open("luts/learning_python_1/data/chapter5.py")]

print(lines)
print()
print([line.upper() for line in open("luts/learning_python_1/data/chapter5.py")])
print()
print(
    [line.rstrip().upper() for line in open("luts/learning_python_1/data/chapter5.py")]
)
print()
print([line.split() for line in open("luts/learning_python_1/data/chapter5.py")])
print()
print(
    [line.replace(" ", "!") for line in open("luts/learning_python_1/data/chapter5.py")]
)
print()
print(
    [
        ("sys" in line, line[:5])
        for line in open("luts/learning_python_1/data/chapter5.py")
    ]
)
print()
print(
    [
        line.rstrip()
        for line in open("luts/learning_python_1/data/chapter5.py")
        if line[0] == "p"
    ]
)
print()
print(
    [
        line.rstrip()
        for line in open("luts/learning_python_1/data/chapter5.py")
        if line.rstrip()[-1:].isdigit()
    ]
)

fname = r"luts/learning_python_1/data/chapter5.py"

print(len(open(fname).readlines()))
print(len([line for line in open(fname) if line.strip() != ""]))
print([x + y for x in "abc" for y in "lmn"])
print(list(map(str.upper, open("luts/learning_python_1/data/chapter5.py"))))
print(sorted(open("luts/learning_python_1/data/chapter5.py")))
print(
    list(
        zip(
            open("luts/learning_python_1/data/chapter5.py"),
            open("luts/learning_python_1/data/chapter5.py"),
        )
    )
)
print(list(enumerate(open("luts/learning_python_1/data/chapter5.py"))))
print(list(filter(bool, open("luts/learning_python_1/data/chapter5.py"))))
print(functools.reduce(operator.add, open("luts/learning_python_1/data/chapter5.py")))
print(list(open("luts/learning_python_1/data/chapter5.py")))
print(tuple(open("luts/learning_python_1/data/chapter5.py")))
print("&&".join(open("luts/learning_python_1/data/chapter5.py")))
print(set(open("luts/learning_python_1/data/chapter5.py")))
print({line for line in open("luts/learning_python_1/data/chapter5.py")})
print(
    {
        ix: line
        for ix, line in enumerate(open("luts/learning_python_1/data/chapter5.py"))
    }
)
print(
    {line for line in open("luts/learning_python_1/data/chapter5.py") if line[0] == "p"}
)
print(
    {
        ix: line
        for ix, line in enumerate(open("luts/learning_python_1/data/chapter5.py"))
        if line[0] == "p"
    }
)
print(list(line.upper() for line in open("luts/learning_python_1/data/chapter5.py")))
print(line.upper() for line in open("luts/learning_python_1/data/chapter5.py"))
print(min(open("luts/learning_python_1/data/chapter5.py")))
print(max(open("luts/learning_python_1/data/chapter5.py")))

Z = zip((1, 2), (3, 4))

print(Z)
print(list(Z))

R = range(10)

print(R)

I = iter(R)

print(next(I))
print(next(I))
print(next(I))
print(list(range(10)))
print(len(R))
print(R[0])
print(R[-1])
print(next(I))
print(I.__next__())
print(len(R))

M = map(abs, (-1, 0, 1))

print(M)
print(next(M))
print(next(M))
print(next(M))

for x in M:
    print(x)

M = map(abs, (-1, 0, 1))

for x in M:
    print(x)

print(list(map(abs, (-1, 0, 1))))


Z = zip((1, 2, 3), (10, 20, 30))

print(Z)
print(list(Z))

for pair in Z:
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))

for pair in Z:
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))

print(next(Z))
print(next(Z))
print(next(Z))

print(list(filter(bool, ["spam", "", "Ni!"])))

R = range(3)
I1 = iter(R)
I2 = iter(R)

print(next(I1))
print(next(I1))
print(next(I2))
print(next(I1))

Z = zip((1, 2, 3), (10, 20, 30))
I1 = iter(Z)
I2 = iter(Z)

print(next(I1))
print(next(I1))
print(next(I2))

M = map(abs, (-1, 0, 1))
I1 = iter(M)
I2 = iter(M)

print(next(I1))
print(next(I1))
print(next(I2))

R = range(3)
I1 = iter(R)
I2 = iter(R)

print(next(I1))
print(next(I1))
print(next(I1))
print(next(I2))

D = dict(a=1, b=2, c=3)

print(D)

K = D.keys()

print(K)

I = iter(K)

print(next(I))
print(next(I))

for k in D.keys():
    print(k, end=" ")

print()

print(list(K))

V = D.values()

print(V)
print(list(V))
print(list(V)[0])
print(list(D.items()))

for k, v in D.items():
    print(k, v, end=" ")

print()

I = iter(D)

print(next(I))
print(next(I))
print(D)

for k in sorted(D.keys()):
    print(k, D[k], end=" ")


print()

for k in sorted(D):
    print(k, D[k], end=" ")
