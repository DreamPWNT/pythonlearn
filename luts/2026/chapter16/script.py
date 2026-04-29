from inter1 import intersect


def times(x, y):
    return x * y


print(times(2, 4))

x = times(3.14, 4)

print(x)
print(times('Py', 4))

s1 = 'HACK'
s2 = 'CHOK'

print(intersect(s1, s2))
print([x for x in s1 if x in s2])
print(intersect([1, 2, 3], (1, 4)))
