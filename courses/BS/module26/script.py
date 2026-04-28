def print_number_info(num):
    """
    Prints num information

    Args:
        num (int): Integer number

    Returns:
        int: Same number
    """
    if num % 2 == 0:
        print('Num is even')
    else:
        print('Num is odd')

    return num


print_number_info(20)

a = 10


def my_fn():
    a = True
    b = 15

    print(a, b)


my_fn()

print(a)

a = 5


def my_fn_2():
    def inner_fn():
        print(a)
    inner_fn()


my_fn()


def global_fn():
    global var

    var = 33


global_fn()

print(var)

c = 5


def another_fn(a, b):
    d = 11

    print(a, b)
    print(c)
    print(dir())


another_fn('abc', 'xyz')

print(dir())
