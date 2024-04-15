import builtins

X = 99


def func(Y):
    Z = X + Y
    return Z


print(func(1))
print(dir(builtins))

X = 88


def func():
    X = 99
    return X


print(func())
print(X)


def func():
    global X
    X = 99
    return X


print(func())
print(X)

X = 99


def f1():
    X = 88

    def f2():
        print(X)

    f2()


f1()


def f1():
    X = 88

    def f2():
        print(X)
        return X

    return f2


action = f1()
print(f1())
print(action())


def maker(N):
    def action(X):
        return X**N

    return action


f = maker(2)
print(f)
print(f(3))
print(f(4))

g = maker(3)
print(g(4))
print(f(4))


def maker(N):
    return lambda X: X**N


h = maker(3)
print(h(4))


def func():
    x = 4
    action = lambda n: x**n
    return action


print("aaaa")
x = func()
print(x(2))


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)

    return acts


acts = makeActions()
print(acts[0])
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[4](2))


def tester(start, operation):
    state = start
    op = operation

    def nested(label):
        nonlocal state
        print(f"{state}. {label}")
        if operation == "+":
            state += 1
        else:
            state -= 1

    return nested


F = tester(0, "+")
print(F("spam"))
print(F("ham"))
print(F("eggs"))

G = tester(10, "-")
print(dir(G))
print(dir(G.__closure__))
print(G("aaa"))
print(G("bbb"))
print(G("ccc"))
