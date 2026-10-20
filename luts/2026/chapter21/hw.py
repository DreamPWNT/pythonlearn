import math


def copyDict(D):
    copied = dict()

    keys = list(D.keys())

    for key in keys:
        copied[key] = D[key]

    return copied


D1 = {'a': 1, 'b': 2, 'c': 534, 'd': 6345}
D2 = {'a': 2, 'g': 543, 'j': 53212, 'l': 12123}


result_dict = copyDict(D1)

print(D1)
print(result_dict)
print(id(D1))
print(id(result_dict))


def addDict(dict1, dict2):
    result = dict()

    for key in list(dict1.keys()):
        result[key] = dict1[key]
    for key in list(dict2.keys()):
        if key not in result:
            result[key] = dict2[key]

    return result


print(addDict(D1, D2))


def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)
def f3(a, **b): print(a, b)
def f4(a, *b, **c): print(a, b, c)
def f5(a, b=2, c=3): print(a, b, c)
def f6(a, b=2, *c): print(a, b, c)


print(f1(1, 2))
print(f1(b=2, a=1))
print(f2(1, 2, 3))
print(f3(1, x=2, y=3))
print(f4(1, 2, 3, **dict(x=2, y=3)))
print(f5(1))
print(f5(1, 4))
print(f5(1, c=4))
print(f6(1))
print(f6(1, *[3, 4]))


def is_prime(num):
    if (num == 0):
        print(num, 'has infinity factors')

    x = num // 2 if num > 0 else num // -2

    while x > 1:
        if num % x == 0:
            print(num, 'has factor', x)
            break
        x -= 1
    else:
        print(num, 'is prime')


print(is_prime(-12))

L = [2, 4, 9, 16, 25]

result = []

for el in L:
    result.append(math.sqrt(el))

print(result)

result = list(map(math.sqrt, L))

print(result)

result = [math.sqrt(el) for el in L]

print(result)

result = (math.sqrt(el) for el in L)

print(list(result))


def countdown(x):
    if x == 0:
        print('stop')
    else:
        print(x)

        x -= 1

        countdown(x)


countdown(9)
