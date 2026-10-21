def countLines(name):
    f = open(name, mode='r', encoding=None)

    return len(f.readlines())


def countChars(name):
    f = open(name, mode='r', encoding=None)

    chars_quantity = 0

    for line in f.read():
        chars_quantity += len(line)

    return chars_quantity


def test(name):
    print(countLines(name))
    print(countChars(name))


if __name__ == '__main__':
    print('lalala')
    test('mymod.py')
