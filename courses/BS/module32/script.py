print((lambda a, b: a * b)(1, 2))


def mult(a, b):
    return a * b


print(mult(10, 5))


def mult(a, b): return a * b


print(mult(10, 5))


def greeting(greet):
    return lambda name: f"{greet} {name}"


morning_greeting = greeting('Good Morning!')
evening_greeting = greeting('Good Evening!')

print(morning_greeting('Vasisualiy'))
print(evening_greeting('Baran'))


def greeting(greet):
    def info(name):
        return f"{greet} {name}"

    return info


morning_greeting = greeting('Good Morning!')
evening_greeting = greeting('Good Evening!')

print(morning_greeting('Vasisualiy'))
print(evening_greeting('Baran'))
