import sys


def print3(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    end = kwargs.get("end", "\n")
    file = kwargs.get("file", sys.stdout)
    output = ""
    first = True

    for arg in args:
        output += ("" if first else sep) + str(arg)
        first = False

    file.write(output + end)
