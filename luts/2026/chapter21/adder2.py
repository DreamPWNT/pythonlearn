def adder(*args):
    total = None

    if len(args) == 1:
        return args[0]
    else:
        if type(args[0]) is int:
            total = 0
        elif type(args[0]) is float:
            total = 0.0
        elif type(args[0]) is list:
            total = []
        elif type(args[0]) is str:
            total = ''
        elif type(args[0]) is dict:
            total = dict()

    for arg in args:
        total += arg

    return total


print(adder(1, 2, 5, 526, 7, 3, 67, 36))
print(adder(6))
print(adder(3.56, 23634.2345, 246.8423, 2478.8943, 2233.678))
print(adder([1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 23, 7, 8, 34, 46, 8, 8, 43]))
print(adder('Vodka', ' save', ' the', ' world', '!'))
print(adder({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
