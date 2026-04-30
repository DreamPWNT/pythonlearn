import scopes101
import builtins
import thismod
from makeopen import makeopen
import os

FILE_PATH = os.getcwd() + '/luts/2026/chapter09'

print(scopes101.func(1))
print(dir(builtins))
print(len(dir(builtins)), len(
    [x for x in dir(builtins) if not x.startswith('__')]))

X = 88


def func():
    global X

    X = 99


func()

print(X)

y, z = 1, 2


def all_global():
    global x

    x = y + z


print(thismod.test())
print(thismod.var)

X = 99


def f1():
    X = 88

    def f2():
        print(X+1)

    f2()


f1()


def f1():
    X = 88

    def f2():
        print(X + 1)

    return f2


action = f1()
action()
action()
action()
action()


def maker(N):
    def action(X):
        return X ** N

    return action


f = maker(2)

print(f)
print(f(3))
print(f(4))

g = maker(3)

print(g(4))
print(g(5))


def maker(N):
    return lambda X: X * N


h, i = maker(2), maker(3)

print(h('Py'), i('Py'))


def f1():
    x = 99

    def f2():
        def f3():
            print(x)

        f3()
    f2()


f1()


def outer(start):
    state = start

    def inner(label):
        print(label, state)

    return inner


F = outer(0)

print(F('code'))
print(F('hack'))


def outer(start):
    state = start

    def inner(label):
        nonlocal state
        state += 1
        print(label, state)

    return inner


F = outer(0)

print(F('code'))
print(F('hack'))

G = outer(24)

print(G('code'))
print(G('hack'))
print(F('more'))


def outer(start):
    state = start

    def inner(label):
        nonlocal state

        state += 1

        print(label, state)

    return inner


F = outer(0)

print(F('nonlocal1'))
print(F('nonlocal2'))


def outer(start):
    global state
    state = start

    def inner(label):
        global state

        state += 1

        print(label, state)

    return inner


F = outer(0)

print(F('global1'))
print(F('global2'))
print(state)

G = outer(24)

print(G('global3'))
print(G('global4'))


def outer(start):
    def inner(label):
        inner.state += 1

        print(label, inner.state)

    inner.state = start

    return inner


F = outer(0)

print(F('attr1'))
print(F('attr2'))

G = outer(24)

print(G('attr3'))
print(F('attr4'))
print(F.state)
print(G.state)
print(F is G)
print(type(F), type(G))
print(id(F), id(G))


def makeActions():
    acts = []

    for i in range(5):
        acts.append(lambda x: i ** x)

    return acts


acts = makeActions()

print(acts[0])

print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))


def makeActions():
    acts = []

    for i in range(5):
        acts.append(lambda x, i=i: i ** x)

    return acts


acts = makeActions()

print(acts[0])

print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

X = 'Hack'


def func():
    X = 'Py!'
    print(X)


func()
print(X)

F = open(f'{FILE_PATH}/datafile.txt')
print('In File!!!\n')
print(F.read())

makeopen('MOD1')

F = open(f'{FILE_PATH}/datafile.txt')

print(F.read())

makeopen('MOD2')

F = open(f'{FILE_PATH}/datafile.txt')

print(F.read())
