import os

FILE_PATH = os.getcwd() + '/luts/2026/chapter14'

for x in [1, 2, 3, 4]:
    print(x ** 2, end=' ')

print()

for x in [1, 2, 3, 4]:
    print(x ** 3, end=' ')

print()

for x in 'text':
    print(x * 2, end=' ')

print()

for k in dict(a=1, b=2, c=3):
    print(k, end=' ')

print()

f = open(f'{FILE_PATH}/data.txt', 'w')

f.write('Testing file IO\n')
f.write('Learning Python, 6E\n')
f.write('Python 3.12\n')

f.close()

f = open(f'{FILE_PATH}/data.txt')

print(f.readline())
print(f.readline())
print(f.readline())

f = open(f'{FILE_PATH}/data.txt')

print(f.__next__())
print(f.__next__())
print(f.__next__())

f.close()

for line in open(f'{FILE_PATH}/data.txt'):
    print(line.upper(), end='')

f = open(f'{FILE_PATH}/data.txt')

print(f.__next__())
print(next(f))
print(next(f))

f = open(f'{FILE_PATH}/data.txt')

print(type(f))

I = iter(f)

print(type(I))
print(next(I))
print(next(I))

L = [1, 2]
I = iter(L)

print(type(I))
print(next(I))
print(next(I))

L = [1, 2, 3]

print(iter(L) is L)

I = iter(L)

print(next(I))

L = [1, 2, 3]

for X in L:
    print(X ** 2, end=' ')

print()

I = iter(L)

while True:
    try:
        X = next(I)
    except StopIteration:
        break

    print(X ** 2, end=' ')

print()

f = open(f'{FILE_PATH}/data.txt')
I = iter(lambda: f.read(5), '')

for block in I:
    print(block, end='')

D = dict(a=1, b=2)

for key in D:
    print(key, D[key])

I = iter(D)

print(next(I))
print(next(I))

R = range(5)

print(R)

I = iter(R)

print(next(I))
print(next(I))

E = enumerate('text')

print(iter(R) is R)
print(iter(E) is E)
print(next(E))
print(next(E))
print(next(E))
print(next(E))

Z = zip((1, 2, 3), (10, 20, 30))

print(Z)
print(next(Z))
print(next(Z))
print(next(Z))

Z = zip(range(1, 4), range(10, 40))

print(next(Z))
print(next(Z))
print(next(Z))

print(list(enumerate(range(1, 4))))
print(list(zip(enumerate(range(1, 4)), enumerate(range(5, 8)))))

for x in enumerate(zip(range(1, 4), range(5, 8))):
    print(x)

print(ord('p'))

M = map(ord, 'py3')

print(next(M))
print(next(M))
print(next(M))

M = map(ord, 'py3')

for x in M:
    print(x, end=' ')

print()
print(filter(bool, ['lp6e', '', 2024]))
print(list(filter(bool, ['lp6e', '', 2024])))
print(list(filter(str.isdigit, ['lp6e', '', '2024'])))
print([ord(x) for x in 'py3'])
print([x for x in ['lp6e', '2024'] if x.isdigit()])

Z = zip((1, 2, 3), (10, 11, 12))

I1 = iter(Z)
I2 = iter(Z)

print(I1 == I2)
print(I1 is I2)
print(next(I1))
print(next(I2))

L = [1, 2, 3, 4, 5]

print(L)

for i in range(len(L)):
    L[i] += 10

print(L)

L = [x + 10 for x in L]

print(L)

f = open(f'{FILE_PATH}/data.txt')

lines = f.readlines()

print(lines)

lines = [line.rstrip() for line in lines]

print(lines)

lines = [line.rstrip() for line in open(f'{FILE_PATH}/data.txt')]

print(lines)

print([line.upper() for line in open(f'{FILE_PATH}/data.txt')])
print([line.rstrip().upper() for line in open(f'{FILE_PATH}/data.txt')])
print([line.split() for line in open(f'{FILE_PATH}/data.txt')])
print([line.replace('\n', '!') for line in open(f'{FILE_PATH}/data.txt')])
print([('Py' in line, line.split()[0])
      for line in open(f'{FILE_PATH}/data.txt')])

lines = [line.rstrip() for line in open(
    f'{FILE_PATH}/data.txt') if line[0].lower() in ['p', 'l']]

print(lines)

print([x + y for x in 'abc' for y in '123'])
