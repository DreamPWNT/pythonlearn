import sys

print(dir(sys))
print(len(dir(sys)))
print(len([x for x in dir(sys) if not x.startswith("__")]))
print(len(dir([])), len([x for x in dir([]) if not x.startswith("__")]))
print(dir(""))


def square(x):
    """square

    Args:
        x (int): int number

    Returns:
        int: sqaure of int
    """
    return x * x


print(sys.__doc__)
print(sys.getrefcount.__doc__)
print(iter.__doc__)

print(help(sys.getrefcount))
print(help("re"))
print(help(sys))
print(help(dict))
print(help(square))

S = input()
chars_sum = 0
ords_list = []

for ch in S:
    print(ord(ch), end=" ")
    chars_sum += ord(ch)
    ords_list.append(ord(ch))

print()
print(f"Sum of ords = {chars_sum}")
print(ords_list)

print([ord(ch) for ch in S])
print(map(ord, S))

for i in range(50):
    print("hello %d\n\a" % i)

D = {
    "g": 1,
    "b": 1,
    "a": 5,
    "n": 123,
    "q": 1,
    "o": 432,
    "x": 12,
    "f": 523,
    "t": 1,
    "z": 321,
}

print({k: v for k, v in sorted(D.items())})

L = [1, 2, 4, 8, 16, 32, 64]
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
found = False
i = 0

while i < len(L):
    if 2**X == L[i]:
        print("at index", i)
        break
    i = i + 1

L = [1, 2, 4, 8, 16, 32, 64]

for x in L:
    if 2**X == L[L.index(x)]:
        print("at index", L.index(x))
        break
else:
    print(X, "not found")

if 2**X in L:
    print("at index", L.index(2**X))
else:
    print(X, "not found")

L = []
X = 5

for i in range(10):
    L.append(2**i)

print(L)

for x in L:
    if 2**X == x:
        print("at index", L.index(x))
        break
else:
    print("not found")
