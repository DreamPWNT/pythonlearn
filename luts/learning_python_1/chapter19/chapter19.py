def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([1, 2, 3, 4, 5]))


def mysum(L):
    return L[0] + mysum(L[1:]) if L else 0


print(mysum([1, 2, 3, 4, 5]))


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, 2, [3, 4, 5, 6, [23, 56, 2, 26, 0], [3, 6, 1, 6]], 2, 6, [1, 5, 6, 12, 3, 6]]

print(sumtree(L))


def sumtree(L):
    tot = 0
    items = list(L)

    while items:
        print("items:", items)
        first = items.pop(0)
        print("first:", first)
        if not isinstance(first, list):
            tot += first
        else:
            items.extend(first)
    return tot


print(sumtree(L))
