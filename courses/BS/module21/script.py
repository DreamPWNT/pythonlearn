from copy import deepcopy

my_number = 1054334345673451252342342345
other_number = 1054334345673451252342342345

print(id(my_number))
print(id(other_number))

first_num = 10
second_num = first_num

print(id(first_num))
print(id(second_num))

second_num += 5

print(first_num)
print(second_num)
print(id(first_num))
print(id(second_num))

my_list = [1, 2, 3]
other_list = [1, 2, 3]

print(id(my_list))
print(id(other_list))
print(id([1, 2, 3]))

other_list.append(4)

print(my_list)
print(other_list)
print(id(my_list))
print(id(other_list))

info = {
    'name': 'Pushist',
    'is_instructor': True
}

info_copy = info

print(id(info))
print(id(info_copy))

info['reviews_qty'] = 5

print(info)
print(info_copy)

info_copy['is_instructor'] = 100

print(info)
print(info_copy)

my_info = {
    'name': 'Pushist',
    'is_instructor': True
}

other_info = {
    'name': 'Pushist',
    'is_instructor': True
}

my_info['post'] = 'Senior DevOps'

print(my_info)
print(other_info)

my_info = {
    'name': 'Pushist',
    'is_instructor': True
}

info_copy = my_info.copy()

info_copy['post'] = 'Debil'

print(my_info)
print(info_copy)

info = {
    'name': 'Pushist',
    'is_instructor': True,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append('Great Job!')

print(info)
print(info_copy)

info = {
    'name': 'Pushist',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great Job!')
info_deepcopy['reviews'].append('Super!')

print(info)
print(info_deepcopy)
