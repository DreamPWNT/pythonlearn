from collections import namedtuple

import os
import pickle
import json
import struct
import csv

FILE_PATH = os.getcwd() + '/luts/2026/chapter09'


print((1, 2) + (3, 4))
print((1, 2) * 4)

T = (1, 2, 3, 4)

print(T[0], T[1:3])
print(T == (1, 2, 3, 4), T > (1, 2, 3, 4), T > (1, 2, 3))

L = ['code', 'hack']

print(*L, 1, 2, *(3, 4))

a, b, c = 1, 2, 3

print(a, b, c)

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)

tmp.sort()

print(tmp)

T = tuple(tmp)

print(T)
print(sorted(T, reverse=True))

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]

print(T, L)
print(tuple(x + 2 for x in T))

T = (1, 2, 3, 2, 4, 2)

print(T.index(2))
print(T.index(2, 2))
print(T.count(2))

T = (1, [2, 3], 5)

T[1][0] = 'mod'

print(T)

pat = ('Pat', 40.5, ['dev', 'mgr'])

print(pat)
print(pat[0], pat[2])

pat = dict(name='Pat', age=40.5, jobs=['dev', 'mgr'])

print(pat['name'], pat['jobs'])
print(tuple(pat.values()))
print(list(pat.items()))

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])

pat = Rec('Pat', age=40.5, jobs=['dev', 'mgr'])

print(pat)
print(pat[0], pat[2])
print(pat.name, pat.jobs)

D = pat._asdict()

print(D['name'], D['jobs'])
print(D)

myfile = open(f'{FILE_PATH}/myfile.txt', 'w')

myfile.write('hello text file\n')
myfile.write('goodbye text file\n')

myfile.close()

myfile = open(f'{FILE_PATH}/myfile.txt')

print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

myfile.close()

print(open(f'{FILE_PATH}/myfile.txt').read())

for line in open(f'{FILE_PATH}/myfile.txt'):
    print(line, end='')

myfile = open(f'{FILE_PATH}/myfile2.txt', 'w')

myfile.write(str(3.14) + '\n')

myfile.close()

print(open(f'{FILE_PATH}/myfile2.txt').read())

myfile = open(f'{FILE_PATH}/myfile3.bin', 'wb')

myfile.write(b'\x00\x01hack\x02\x03')

myfile.close()

data = open(f'{FILE_PATH}/myfile3.bin', 'rb').read()

print(data)
print(data[2:6])

byte = data[2:6][0]

print(byte, chr(byte), bin(byte))

X, Y, Z = 62, 63, 64
S = 'Text'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open(f'{FILE_PATH}/datafile.txt', 'w')

F.write(S + '\n')
F.write(f'{X},{Y},{Z}\n')
F.write(str(L) + '$' + str(D) + '\n')

F.close()

chars = open(f'{FILE_PATH}/datafile.txt').read()

print(chars)
print(repr(chars))

F = open(f'{FILE_PATH}/datafile.txt')

line = F.readline()

print(repr(line))
print(repr(line.rstrip()))

line = F.readline()

print(repr(line))

parts = line.rstrip().split(',')

print(parts)

numbers = [int(P) for P in parts]

print(numbers)

line = F.readline()

print(line)

parts = line.split('$')

print(eval(parts[0]))

D = {'a': 1, 'b': 2}

F = open(f'{FILE_PATH}/datafile.pkl', 'wb')

pickle.dump(D, F)

F.close()

F = open(f'{FILE_PATH}/datafile.pkl', 'rb')

E = pickle.load(F)

print(E)
print(open(f'{FILE_PATH}/datafile.pkl', 'rb').read())

who = dict(first='Pat', last='Smith')
rec = dict(name=who, job=['dev', 'mgr'], age=40.5)

print(rec)

print(json.dumps(rec))

S = json.dumps(rec)
O = json.loads(S)

print(O)
print(O == rec)

file = open(f'{FILE_PATH}/testjson.txt', 'w')

json.dump(rec, fp=file, indent=4)

file.close()

print(open(f'{FILE_PATH}/testjson.txt').read())

P = json.load(open(f'{FILE_PATH}/testjson.txt'))

print(P)
print(P == rec)

data = struct.pack('i6s', 62, b'Python')

print(data)

file = open(f'{FILE_PATH}/data.bin', 'wb')

file.write(data)

file.close()

print(struct.unpack('i6s', open(f'{FILE_PATH}/data.bin', 'rb').read()))

rdr = csv.reader(open(f'{FILE_PATH}/customers-100.csv'))

for row in rdr:
    print(row)

with open(f'{FILE_PATH}/datafile.txt') as myfile:
    for line in myfile:
        print(line)

myfile = open(f'{FILE_PATH}/datafile.txt')

try:
    for line in myfile:
        print(line)
finally:
    myfile.close()

L = ['abc', [(1, 2), ([3], 4), 5]]

print(L[1], L[1][1], L[1][1][0], L[1][1][0][0])

X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}

print(X, L, D)

X[1] = 'surprise'

print(X, L, D)

L = [1, 2, 3]
D = {'a': 1, 'b': 2}

A = L[:]
B = D.copy()

print(L, D, A, B)

A[1] = 'Py'
B['c'] = 'code'

print(L, D, A, B)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]

print(L1 == L2, L1 is L2)

S1 = 'text'
S2 = 'text'

print(S1 == S1, S1 is S2)

S1 = 'a longer string'
S2 = 'a longer string'

print(S1 == S2, S1 is S2)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]

print(L1 < L2, L1 == L2, L1 > L2)

print(11 == '11')
print(11 > 9.123)
print(str(11) >= '11', 11 >= int('11'))

D1 = {'b': 3, 'a': 1}
D2 = {'a': 1, 'b': 3}

print(D1 == D2)

print(list(D1.items()))
print(sorted(D1.items()))

print(sorted(D1.items()) < sorted(D2.items()))
print(sorted(D1.items()) >= sorted(D2.items()))

size = 50
L = [None] * size

L[size - 1] = 'OK'

print(L[-10:])

print(bool(1))
print(bool('text'))
print(bool({}))

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(L)
print(X)
print(Y)

L[1] = 'vodochka!!!!!'

print(Y)

L = [4, 5, 6]
Y = [list(L)] * 4

print(Y)
print(id(Y[0]), id(Y[1]), id(Y[2]), id(Y[3]))

Y[0][2] = 'Seledochka!!!'

print(Y)

L = [4, 5, 6]
Y = [list(L) for i in range(4)]

print(Y)

Y[0][1] = 'Locman'

print(Y)

L = ['stuff']
L.append(L)

print(L)
