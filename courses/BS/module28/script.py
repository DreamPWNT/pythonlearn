print(not 10)
print(not 0)
print(not 'abc')
print(not '')
print(not True)
print(not False)
print(not not 10)
print(not not 0)
print(not not 'abc')
print(not not '')
print(not not True)
print(not not False)

print(1 and 2)
print([] and 2)
print(1 or 2)
print([] or 2)
print({} or [])

my_list = [1, 2]
other_list = ['a', 'b']

print(my_list or other_list)
print(len(my_list) > 0 or other_list)
print(len(my_list) < 0 or other_list)
print(len(my_list) < 0 or other_list[0])

my_dict = {'a': 1}

print(my_list and my_dict)
print(bool(my_list and my_dict))

my_list and print('List is not empty')
my_dict and print('Dict is not empty')

my_dict = {'a': 1, 'b': 2}
my_dict_2 = {'b': 2, 'a': 1}

my_dict == my_dict_2 and print('Dictionary is equal')
