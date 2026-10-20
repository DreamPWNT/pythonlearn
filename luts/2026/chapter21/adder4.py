def adder(**kwargs):
    total = None

    keys = list(kwargs.keys())
    values = list(kwargs.values())

    if len(kwargs) == 1:
        return values[0]
    else:
        if type(values[0]) is int:
            total = 0
        elif type(values[0]) is float:
            total = 0.0
        elif type(values[0]) is list:
            total = []
        elif type(values[0]) is str:
            total = ''

    for key in keys:
        total += kwargs[key]

    return total


print(adder(a=1, b=2, fds=67345, gsdrffg=234523456))
print(adder(a='gfd', b='tttt', c='3255252'))
print(adder(a=2.467, b=2345.7467, dgf=654.7654, sdf=212.2246784))
print(adder(a=[1, 67, 3, 56, 78], b=[-432, 2, 67, 2, 7], c=['a', 'fgsdfasd']))
