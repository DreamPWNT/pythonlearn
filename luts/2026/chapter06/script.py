import copy
import sys

a = 3
b = a
a = 'hack'

print(a, b)

L1 = [2, 3, 4]
L2 = L1

print(L1, L2)

L1 = 24

print(L1, L2)

L1 = [2, 3, 4]
L2 = L1

print(id(L1), id(L2))

L1[0] = 24

print(L1, L2)
print(id(L1), id(L2))

L1 = [2, 3, 4]
L2 = L1[:]

print(L1, L2)
print(id(L1), id(L2))

L1[0] = 24

print(L1, L2)
print(id(L1), id(L2))

L = [1, 2, 3]
M = L

print(M == L)
print(L is M)

L = [1, 2, 3]
M = [1, 2, 3]

print(M == L)
print(L is M)

X = 99
Y = 99

print(X == Y)
print(X is Y)

print(sys.getrefcount(99))
print(sys.getrefcount(2 ** 1000))

print(id(99) == id(99))
