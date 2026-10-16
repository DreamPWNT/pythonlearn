import sys


def f(a):
    a = 99


b = 88

print(f(b))
print(b)


def changer(a, b):
    a = 2
    b[0] = 'mod'


X = 1
L = [1, 2]

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


def f(a, b, c): print(a, b, c)


f(1, 2, 3)
f(c=3, b=2, a=1)
f(1, c=3, b=2)


def f(a, b=2, c=3): print(a, b, c)


f(1)
f(a=33)
f(1, 4)
f(1, 4, 5)
f(1, c=66)


def func(code, hack, script=0, app=0):
    print((code, hack, script, app))


func(1, 2)
func(1, app=1, hack=0)
func(code=1, hack=0)
func(script=1, hack=2, code=3)
func(1, 2, 3, 4)


def func(code, hack, script=0, app=0): return (code, hack, script, app)


print(func(1, 2))
print(func(script=1, hack=2, code=3))


def f(*args): print(args)


f()
f(1)
f(1, 2, 3, 4)


def f(**kwargs): print(kwargs)


f()
f(a=1, b=2)


def f(a, *args, **kwargs): print(a, args, kwargs)


f(1, 2, 3, x=1, y=2, z=5)


def func(a, b, c, d): print(a, b, c, d)


args = (1, 2)
args += (3, 4)

func(*args)

kwargs = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

func(**kwargs)
func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *[2, 3], **dict(d=4))
func(1, c=3, *[2], **{'d': 4})
func(1, *(2, 3), d=4)
func(1, *[2], c=3, **dict(d=4))

args, kwargs = (1, 2), dict(d=4, c=3)

func(*args, **kwargs)


def func(a, b, c, d): print(a, b, c, d)


func(*[1], *(2,), **dict(c=3), **{'d': 4})
func(*[1], *(2,), *[3, 4])
func(**dict(a=1, b=2), **dict(c=3), **{'d': 4})
func(*[1], 2, **dict(c=3), d=4)


def tracer(func, *args, **kwargs):
    print('calling:', func.__name__)
    return func(*args, **kwargs)


def func(a, b, c, d): return a + b + c + d


print(tracer(func, 1, 2, c=3, d=4))


def kwonly(a, *b, c): print(a, b, c)


kwonly(1, 2, c=3)
kwonly(a=1, c=3)


def kwonly(a, *, b, c): print(a, b, c)


kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)


def kwonly(a, *, b='code', c='app'): print(a, b, c)


kwonly(1)
kwonly(1, c='hack')
kwonly(a='py')
kwonly(c=3, b=2, a=1)


def kwonly(a, *, b, c='hack'): print(a, b, c)


kwonly(1, b='code')


def kwonly(a, *, b=2, c, d=4): print(a, b, c, d)


def mostlypos(a, b, /, c): print(a, b, c)


mostlypos(1, 2, 3)
mostlypos(1, 2, c=3)


def allpos(a, b, c, /): print(a, b, c)


allpos(1, 2, 3)

f = lambda a, b, /, c: print(a, b, c)

f(1, 2, c=3)


def combo(a, b, /, *, c, d): print(a, b, c, d)


combo(1, 2, c=3, d=4)


def f(a, /, b, c=3, *ps, e=4, **ks): \
    print(f'{a=}, {b=}, {c=}, {ps=}, {e=}, {ks=}')


f(0, 1, 2, 3, 4, e=5, f=6, g=7)


def f(a, b, c, d, e, f, g, h, i):
    print(a, b, c, d, e, f, g, h, i)


f(*[1], 2, *[3], 4, f=6, *[5], **dict(g=7), h=8, **{'i': 9})


def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)

    output = ''
    first = True

    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False

    file.write(output + end)


print3(1, 2, 3)
print3(1, 2, 3, sep='')
print(1, 2, 3, sep='...')
