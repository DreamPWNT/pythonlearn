x = 'code'

while x:
    print(x, end=' ')
    x = x[1:]

a = 0
b = 10

print('\n', end='')

while a < b:
    print(a, end=' ')

    a += 1

print('\n', end='')

x = 10

while x:
    x -= 1

    if x % 2 != 0:
        continue

    print(x, end=' ')

print('\n', end='')

x = 10

while x:
    x -= 1

    if x % 2 == 0:
        print(x, end=' ')

# num = 1

# while True:
#     tool = input(f'{num} What\'s your favorite language? ')

#     if tool == 'stop':
#         break

#     print('Bravo!' if tool == 'Python' else 'Try again...')

#     num += 1

num = 20
x = num // 2

while x > 1:
    if num % x == 0:
        print(num, 'has factor', x)
        break

    x -= 1
else:
    print(num, 'is prime')

for x in ['app', 'script', 'program']:
    print(x, end=' ')

print()

sum = 0

for x in [1, 2, 3, 4]:
    sum += x

print(sum)

prod = 1

for item in [1, 2, 3, 4]:
    prod *= item

print(prod)

S = 'Python'
T = ('web', 'num', 'app')

for x in S:
    print(x, end=' ')

print()

for x in T:
    print(x, end=' ')

print()

T = [(1, 2), (3, 4), (5, 6)]

for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2}

for key in D:
    print(key, '=>', D[key])

print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)

for both in T:
    a, b = both

    print(a, b)

((a, b), c) = ((1, 2), 3)

print(a, b, c)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]:
    print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], list(all[1:-1]), all[-1]

    print(a, b, c)

L, M = [1, 2], [3, 4]
pairs = [[(5, 6), (7, 8), (9, 10)]] * 5

print(L)
print(M)
print(pairs)

for [(a, *X), (b, *L[0]), (c, *M[:0])] in pairs:
    print(f'<{a=}> {X=}> <{b=} {L=}> <{c=} {M=}>')

for x in 'abc':
    for y in '123':
        print(x + y, end=' ')

print()

items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found')

            break
    else:
        print(key, 'not found')

for key in tests:
    if key in items:
        print(key, 'was found')
    else:
        print(key, 'not found')

seq1 = 'trippy'
seq2 = 'python'

res = []

for x in seq1:
    if x in seq2:
        res.append(x)

print(list(set(seq1) & set(seq2)))
print([x for x in seq1 if x in seq2])
print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
print(range(5)[2], range(5)[1:3], list(range(5)) + [6, 7])
print(list(range(-5, 5)))
print(list(range(5, -5, -1)))

X = 'hack'

for item in X:
    print(item, end=' ')

print()

i = 0

while i < len(X):
    print(X[i], end=' ')

    i += 1

print()

i = -1

while (i := i + 1) < len(X):
    print(X[i], end=' ')

print()

print(X, len(X))
print(list(range(len(X))))

for i in range(len(X)):
    print(X[i], end=' ')

print()

S = 'hack'

for i in range(len(S)):
    S = S[1:] + S[:1]

    print(S, end=' ')

print()

for i in range(len(S)):
    X = S[i:] + S[:i]

    print(X, end=' ')

print()

L = [1, 2, 3, 4]

for i in range(len(L)):
    X = L[i:] + L[:i]

    print(X, end=' ')

print()

S = 'abcdefghijk'

print(list(range(0, len(S), 2)))

for i in range(0, len(S), 2):
    print(S[i], end=' ')

print()

for c in S[::2]:
    print(c, end=' ')

print()

L = [10, 20, 30, 40, 50]

for x in L:
    x += 1

print(L, x)

for i in range(len(L)):
    L[i] += 1

print(L)

i = 0

while i < len(L):
    L[i] += 1
    i += 1

print(L)
print(x + 1 for x in L)

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print(zip(L1, L2))
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(f'{x} + {y} => {x + y}')

print(list(zip(range(4), 'hack')))

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (6, 7, 8)

print(T3)
print(list(zip(T1, T2, T3)))

S1 = 'abc'
S2 = 'xyz123'

print(list(zip(S1, S2)))

D1 = {'app': 1, 'script': 3, 'program': 5}

print(D1)

keys = ['app', 'script', 'program']
vals = [1, 3, 5]

print(list(zip(keys, vals)))

D2 = {}

for (k, v) in zip(keys, vals):
    D2[k] = v

print(D2)

D3 = dict(zip(keys, vals))

print(D3)
print({k: v for (k, v) in zip(keys, vals)})

S = 'hack'
offset = 0

for item in S:
    print(item, 'appears at offset', offset)

    offset += 1

S = 'hack'

for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

E = enumerate(S)

print(E)

print(next(E))
print(next(E))
print(next(E))
print([c * i for (i, c) in enumerate(S)])


for (ix, line) in enumerate(open('data.txt')):
    print(f'{ix}) {line.rstrip()}')

file = open('data.txt')

print(file.read())

for char in open('data.txt').read():
    print(char, end='')

print()

file = open('data.txt')

while char := file.read(1):
    print(char, end='')

file = open('data.txt')

while line := file.readline():
    print(line.rstrip())

file = open('data.txt')

while chunk := file.read(10):
    print(chunk, end='')

for line in open('data.txt').readlines():
    print(line.rstrip())

for line in open('data.txt'):
    print(line.rstrip())
