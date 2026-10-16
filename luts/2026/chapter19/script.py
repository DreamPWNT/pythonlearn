def mysum(L):
    print(L)
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])


print(mysum([1, 2, 3, 4, 5]))
print(mysum(['a', 't', 'a', 't', 'a']))

print(*[1, 2, 3, 4, 5])

L = [1, [2, [3, 4], 5], 6, [7, 8]]


def sumtree(L, trace=False):
    tot = 0

    for x in L:
        if not isinstance(x, list):
            tot += x

            if trace:
                print(x)
        else:
            tot += sumtree(x, trace)

    return tot


print(sumtree(L))
print(sumtree(L, True))

print(L)
print()


def sumtree(L, trace=False):
    tot = 0
    items = list(L)

    while items:
        front = items.pop(0)

        if not isinstance(front, list):
            print("front", front)
            print("items", items)
            tot += front
        else:
            print("front", front)
            print("items", items)
            items.extend(front)
            print("items", items)

    return tot


print(sumtree(L))


def sumtree(L, trace=False):
    tot = 0
    items = list(L)

    while items:
        front = items.pop(0)

        if not isinstance(front, list):
            print("front", front)
            print("items", items)
            tot += front
        else:
            print("front", front)
            print("items", items)
            items[:0] = front
            print("items", items)

    return tot


print(sumtree(L))

L3 = [5, 6, 7, 8]
L3[:0] = [1, 4, 67, 23]

print(L3)


def func(a):
    b = 'Hack'

    return b * a


print(func(3))

print(func.__name__)
print(dir(func))
print(func.__code__)
print(dir(func.__code__))
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)

func.vodka = 'Seledka'

print(dir(func))
print(func.vodka)
