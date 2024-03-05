import sys
import re

print(sys.platform)
print(2 ** 100)

a = 'Vodka!'

print(a*8)

str1 = 'Vodka   save the   world!'

match = re.match('Vodka[ \t]*(.*)world',str1)
print(match.groups())

str2 = '/usr/bin/php:vodka'

match = re.match('[/:](.*)[/:](.*)[/:](.*)[/:](.*)',str2)
print(match.groups())

match2 = re.split('[/:]',str2)
print(match2)

L = [178,'Vodka',3.33,'save']
print(len(L))
print(L[0])
print(L[:1])
print(L[1:8])

L2 = L + [6.66,'the',10000,'world']
print(L2)

L3 = L2 * 2
print(L3)

L3.append('Seledochka!')
print(L3)

L3.pop(-1)
print(L3)

L4 = ['bb','cc','aa']

L4.sort()
print(L4)

L4.reverse()
print(L4)

L5 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]  
     ]
print(L5)

print(L5[2])
print(L5[0][2])

col3 = [row[2] for row in L5]
print(col3)

col3_2 = [row[2] * 33 for row in L5]
print(col3_2)

col3_3 = [row[2] for row in L5 if row[2] % 2 == 0]
print(col3_3)

diag = [L5[i][i] for i in [0,1,2]]
print(diag)

diag2 = [L5[i][i]+3.33 for i in [0,1,2]]
print(diag2)

vodka_str = 'vodochka!'
double_vodka = [char * 2 for char in vodka_str]
print(double_vodka)

print(list(range(33)))
print(list(range(-67,80,12)))

range_list = [[x ** 2, x ** 3] for x in range(10)]
print(range_list)

G = (sum(row) for row in L5)

print(next(G))
print(next(G))
print(next(G))

L6 = list(map(sum,L5))
print(L6)

L7 = {sum(row) for row in L5}
print(L7)

L8 = {i: sum(L5[i]) for i in range(3)}
print(L8)

print([ord(char) for char in 'Vodochka!!!'])
print({ord(char) for char in 'Vodochka!!!'})

L9 = {3,9,4,5,27,90}
print(L9)