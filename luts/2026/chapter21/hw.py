def copyDict(D):
    copied = dict()

    keys = list(D.keys())

    for key in keys:
        copied[key] = D[key]

    return copied


D1 = {'a': 1, 'b': 2, 'c': 534, 'd': 6345}
D2 = {'a': 2, 'g': 543, 'j': 53212, 'l': 12123}


result_dict = copyDict(D1)

print(D1)
print(result_dict)
print(id(D1))
print(id(result_dict))


def addDict(dict1, dict2):
    result = dict()

    for key in list(dict1.keys()):
        result[key] = dict1[key]
    for key in list(dict2.keys()):
        if key not in result:
            result[key] = dict2[key]

    return result


print(addDict(D1, D2))
