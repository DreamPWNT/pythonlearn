
my_dict = {'a': True, 'b': 10}

print(my_dict)

del my_dict['a']

print(my_dict)

my_dict.__delitem__('b')

print(my_dict.__delitem__)
print(my_dict)

my_list = [1, 2]

del my_list[0]

print(my_list)
