import math
import random
import re

print(math.pi)
print(math.sqrt(69))

print(random.random())
print(random.choice([1,2,5,7,8,4,67,8]))

S = 'Spam'

print(len(S))
print(S[0])
print(S[1])
print(S[-1])
print(S[-2])
print(S[1:3])
print(S[1:])
print(S[:-1])
print(S[0:3])
print(S[:])

print(S + 'xyz')
print(S * 9)

S = 'z' + S[1:]

print(S)

T = 'shruberry'
L = list(T)
print(L)
L[1] = 'c'
print(''.join(L))

B = bytearray(b'spam')
print(B)
B.extend(b'eggs')
print(B)
print(B.decode())

S = 'Spam'
print(S.find('pa'))
print(S.find('pp'))
print(S.replace('pa','XYZ'))

line = 'aaa,bb,cccccc,ddddd'
print(line.split(','))
print(S.upper())
print(S.isalpha())
line = line + "    \n\n\n   \n\n "
print(line)
print(line.rstrip().split(','))

print(dir())

print(S + 'NI!')
print(S.__add__('NI!'))

print('sp\xc4m')
print(b'a\x01c')
print(u'sp\u00c4m')
print('sp\xc5\u00c4\U000000c4m')
print('\u00A3')
print('\u00A3'.encode('latin1'))
print(b'\xA3'.decode('latin1'))

match = re.match('[/:](.*)[/:](.*)[/:](.*)','/usr/home:lumberjack')
print(match.groups())

L = [123, 'spam', 1.23]
print(L)
print(L[0])
print(L[:-1])
print(L + [4,5,6])
print(L * 3)

L.append('NI!')
L.pop(2)

print(L)

M = ['bbb','zzz','aaa']
M.sort()
print(M)
M.reverse()
print(M)

M = [
  [1,5,2],
  [8,23,6],
  [0,3,78]
]
print(M)
print(M[1])
print(M[2][0])

print([row[1] + 3 for row in M])
print([row[0] for row in M if row[0] % 2 == 0])
print([M[i][i] for i in [0,1,2]])

doubles = [c * 2 for c in 'spam']

print(doubles)
print(list(range(9)))
print(list(range(-33,11,6)))
print([[x + 13, x / 66] for x in range(6)])

G = (sum(row) for row in M)

print(next(G))
print(next(G))
print(next(G))
print(list(map(sum,M)))
print({sum(row) for row in M})
print({i: sum(M[i]) for i in range(3)})

