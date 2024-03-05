import math
import random
import re
import decimal
import fractions

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
print([ord(x) for x in 'spaam'])
print({ord(x) for x in 'spaam'})
print({x: ord(x) for x in 'spaam'})

D = {'color':'pink', 'quantity': 4, 'food': 'Caesar salad'}

print(D)

D['quantity'] += 1
D['color'] = 'red'

print(D)

D2 = {}
D2['name'] = 'Vasisualiy'
D2['post'] = 'Senior JavaScript developer'
D2['ages'] = 32

print(D2)

D3 = dict(name='Vasisualiy', post='Senior JavaScript developer', ages=32)
print(D3)
D4 = dict(zip(['name','post','ages'],['Vasisualiy','Senior JavaScript developer',32]))
print(D4)

D5 = {
        'server_name': 'isapra-01-db',
        'db-name': 'dt',
        'roles': ['easapr','admin'],
        'login': 'easapr',
        'password': 'easapr1'
     }

print(D5)

D5['roles'].append('user')

print(D5)
print('sss' in D5)

if not 'sss' in D5:
  print('missingggg')
  print('no key in D5 object')

Ks = list(D5.keys())
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
  print(key, '=>', D5[key])

for char in 'spam':
  print(char.upper())
  
x = 4
while x > 0:
  print('spam' * x)
  x -= 1
  
T = (1,2,3,4,5,4,3,4,56,3,65,3,23,5,6,2,2,6,7,6,2)

print(len(T))
print(T.index(6))
print(T.count(2))
print((2,) + T[13:])

T2 = 11.11, 45, ['s','t','y'], 'Yeeeeep'
print(T2)
print(T2[2])
T2[2].append('z')
print(T2)

f = open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('data.txt','r')
text = f.read()
print(text)

S = 'sp\xc4m'
file = open('unidata.txt','w',encoding='utf-8')
file.write(S)
file.close()
text = open('unidata.txt',encoding='utf-8').read()
print(text)

X = {'s','p','a','m'}
Y = {'a','b','p','d'}

print(X & Y)
print(X | Y)
print(X - Y)
print(Y - X)
print(X > Y)

d = decimal.Decimal('3.14145')
d = d + 1
print(d)

f = fractions.Fraction(2,3)
f = f + 1
print(f)
f = f + fractions.Fraction(1,9)
print(f)

print(type(L))
print(type(type(L)))
print(type(X))
print(type(d))
print(type(f))