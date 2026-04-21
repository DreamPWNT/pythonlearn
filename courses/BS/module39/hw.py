dct = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc', 'd': 'ddd'}

result_dct = {k: v.upper() for k, v in dct.items()}

print(result_dct)

lst = ['aaa', 'bbb', 'ddddd', 'eeeeeeee', 'ffffffffff', 'gg', 'h']

result_lst = [elem for elem in lst if len(elem) > 3]

print(result_lst)
