def f(a):
    a = 99


b = 88

print(f(b))
print(b)


def changer(a, b):
    a = 2
    b[0] = "spam"


X = 1
L = [1, 2]

print(X, L)
print(changer(X, L))
print(X, L)

L = [1, 2]

changer(X, L[:])
print(X, L)
