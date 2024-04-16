def f(a):
    a = 99


b = 88
f(b)
print(b)


def changer(a, b):
    a = 2
    b[0] = "spam"


X = 1
L = [1, 2]

changer(X, L)

print(X, L)

X = 1
L = [1, 2]

changer(X, L[:])

print(X, L)


def changer(a, b):
    b = b[:]
    a = 2
    b[0] = "spam"


changer(X, L)

print(X, L)


def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y


X = 1
L = [1, 2]
X, L = multiple(X, L)

print(X, L)

a, *b, c = [1, 2, 3, 4, 5, 6, 7, 8]

print(a, b, c)


def f(a, b, c):
    print(a, b, c)


x, y, z = 4, 6, 347

print(f(x, y, z))
print(f(c=z, a=y, b=x))
print(f(z, c=y, b=x))


def f(a, b=2, c=3):
    print(a, b, c)


print(f(z))
print(f(a=z))
print(f(z, x))
print(f(z, y, x))
print(f(z, c=x))


def func(spam, eggs, toast=0, ham=0):
    print(spam, eggs, toast, ham)


print(func(1, 2))
print(func(1, ham=1, eggs=0))
print(func(spam=1, eggs=0))
print(func(toast=1, eggs=2, spam=3))
print(func(1, 2, 3, 4))


def f(*args):
    for i in args:
        print(i)


print(f(1, 5, 3, 6, 3, 67, 34, 8))


def f(**kwargs):
    print(kwargs)


print(
    f(
        a=1,
        b=5,
        c=673,
        d=784,
        h=24,
        spam=[
            12,
            5,
            42,
            6,
        ],
        stttr="gcdfsas",
        ddd={1: "sfghsf", (23, 5, 3): "ooooo"},
    )
)


def f(a, *pargs, **kwargs):
    print(a, pargs, kwargs)


print(
    f(
        5,
        7,
        4,
        6,
        7,
        fff=6,
        sss=8,
        jsjhfg=2345,
        ititititi="spspfjnfjsj",
        aaa=1,
        b=5,
        c=673,
        d=784,
        h=24,
        spam=[
            12,
            5,
            42,
            6,
        ],
        stttr="gcdfsas",
        ddd={1: "sfghsf", (23, 5, 3): "ooooo"},
    )
)


def func(a, b, c, d):
    print(a, b, c, d)


args = (1, 2)
args += (3, 4)

func(*args)

args = {"a": 1, "b": "3", "c": "5432"}
args["d"] = 27834

func(**args)

func(*(1, 2), **{"d": 4, "c": 3})
func(1, *(2, 3), **{"d": 4})
func(1, c=3, *(2,), **{"d": 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{"d": 4})


def tracer(func, *pargs, **kwargs):
    print("calling:", func.__name__)
    return func(*pargs, **kwargs)


def func(a, b, c, d):
    print(a, b, c, d)
    return a + b + c + d


print(tracer(func, 1, 2, c=3, d=4))


def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(a=1, c=3)


def kwonly(a, *, b, c):
    print(a, b, c)


kwonly(1, c=2, b=3)


def kwonly(a, *, b="spam", c="ham"):
    print(a, b, c)


kwonly(1)
kwonly(1, b="spam1", c="ham1")


def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, c=7, x=4, y=5)
f(1, 2, 3, x=4)
f(1, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5), c=7)
f(1, *(2, 3), c=7, **dict(x=4, y=5))
f(1, c=7, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5, c=7))


def min1(*args):
    res = args[0]
    for i in args:
        if i < res:
            res = i
    return res


print(min(1, 2, 1, 56, 2, 6, 3, 6, 4))


def inserect(*args):
    res = []
    for el in args[0]:
        print(el)
        if el in res:
            print("continue")
            continue
        else:
            for e in args[1:]:
                print(e)
                if not el in e:
                    break
            else:
                res.append(el)

    return res


print(inserect([1, 2], [2, 3], [2, 4]))


def union(*args):
    res = []
    for el in args:
        for e in el:
            if not e in res:
                res.append(e)

    return res


print(union([1, 2], [2, 3], [2, 4]))
