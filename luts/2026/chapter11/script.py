import sys
import os

FILE_PATH = os.getcwd() + '/luts/2026/chapter11'

target = 'hack'
code, hack = 'py', 'PY'

print(code, hack)

[code, hack] = ['ry', 'RY']

print(code, hack)

a, b, c, d = 'hack'

print(a, b, c, d)

a, *b = 'hack'

print(a, b)
print((python := 3.12) + 0.01)

L = [1, 2]
L[0] = 3
L[-1:] = [4, 5]

print(L)

first = 1
second = 2

A, B = first, second

print(A, B)

[C, D] = [first, second]

print(C, D)

c = first
first = second
second = c

print(first, second)

first, second = second, first

print(first, second)

[a, b, c] = (1, 2, 3)

print(a, c)

(a, b, c) = 'ABC'

print(a, c)

string = 'TEXT'

a, b, c, d = string

print(a, b, c, d)

a, b, c = string[0], string[1], string[2:]

print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]

print(a, b, c)

a, b = string[:2]
c = string[2:]

print(a, b, c)

(a, b), c = string[:2], string[2:]

print(a, b, c)

red, green, blue = range(3)

print(red, blue)

L = [1, 2, 3, 4]

while L:
    front, L = L[0], L[1:]
    print(front, L)

seq = [1, 2, 3, 4]

a, b, c, d = seq

print(a, d)

a, *b = seq

print(a, b)

*a, b = seq

print(a, b)

a, *b, c = seq

print(a, b, c)

a, *b = 'hack'

print(a, b)

a, *b, c = 'hack'

print(a, b, c)

a, *b, c = range(4)

print(a, b, c)

S = 'hack'

a, b, c = S[0], S[1:-1], S[-1]

print(a, b, c)

a, *b, c = S

print(a, b, c)

L = [1, 2, 3, 4]

while L:
    front, *L = L
    print(front, L)

seq = [1, 2, 3, 4]

a, b, c, *d = seq

print(a, b, c, d)

a, b, c, d, *e = seq

print(a, b, c, d, e)

[(a, *b), (c, *d)] = [(1, 2, 3, 4), (5, 6, 7, 8)]

print(a, b, c, d)

[(a, *b, x), (c, *d)] = [(1, 2, 3, 4), (5, 6, 7, 8)]

print(a, b, x, c, d)

a, *L = [1, 2, 3]

print(a, L)

a, *L[0] = [4, 5, 6]

print(a, L)

a, *L[1:] = [7, 8, 9]

print(a, L)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

a = 'hack' * (b := 2)

print(a)

(python := 3.12) + 0.01

print(python)

print([val := 'Py', val * 2, val * 3])
print(list(pow := 2 ** num for num in [2, 4, 8]))
print(pow)
print(f'Hello {(name := input('Who are you? '))}')

(x := (y := (z := 1) + 1) + 1)

print(x, y, z)

print()

x = 'python'
y = 3.12
z = ['lp6e']

print(x, y, z)
print(x, y, z, sep='')
print(x, y, z, sep=', ')
print(x, y, z, end='')
print(x, y, z, end='')
print(x, y, z)
print(x, y, z, end='...\n')
print(x, y, z, sep='...', end='!\n')

print(x, y, z, sep='...', file=open('data.txt', 'w'))
print(x, y, z)
print(open('data.txt').read())

sys.stdout.write('hello world\n')

temp = sys.stdout
sys.stdout = open(f'{FILE_PATH}/log.txt', 'a')

print('lp6e was here')
print(1, 2, 3)

sys.stdout.close()

sys.stdout = temp

print('back in REPL')
print(open(f'{FILE_PATH}/log.txt').read())

log = open(f'{FILE_PATH}/log.txt', 'a')

print(x, y, z, file=log)
print(a, b, c)

X, Y = 1, 2

print(X, Y)

sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

print(X, Y, file=open(f'{FILE_PATH}/temp1', 'w'))
print(open(f'{FILE_PATH}/temp2', 'w').write(str(X) + ' ' + str(Y) + '\n'))
print(open(f'{FILE_PATH}/temp1', 'rb').read())
print(open(f'{FILE_PATH}/temp2', 'rb').read())
