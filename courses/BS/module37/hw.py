def dict_to_list(dct):
    return [(k, v * 2 if type(v) == int else v) for (k, v) in dct.items()]


D = {'a': 22, 'b': 'abg', 'c': True, 'd': 15, 'e': [3, 4, 5]}

print(dict_to_list(D))


def filter_list(lst, lst_type):
    return [el for el in lst if type(el) == lst_type]


L = [1, 5, 2, 'asf', 'dwgt', True, [False, None], {'a': 12341}, (5, 32, 7)]

print(filter_list(L, int))
print(filter_list(L, list))
print(filter_list(L, str))
print(filter_list(L, dict))
print(filter_list(L, bool))
print(filter_list(L, tuple))
print(filter_list(L, set))


def filter_list_2(list_to_filter, value_type):
    def check_element(elem):
        return type(elem) == value_type
    return list(filter(check_element, list_to_filter))


print(filter_list_2(L, int))
print(int.__subclasses__())


def filter_list_3(list_to_filter, value_type):
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))


print(filter_list_3(L, int))
