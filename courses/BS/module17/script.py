my_fruits = ('apple', 'banana', 'lime')
other_fruits = ('banana', 'apple', 'lime')
post_ids = (151, 245, 762, 167)

print(my_fruits == other_fruits)
print(len(my_fruits))
print(post_ids[0])
print(post_ids[1])
print(post_ids[-1])

my_nums = (10, 5, 100, 0)

print(type(my_nums))

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)

print(users[1]['user_id'])

users[1]['user_id'] = 100

print(users[1]['user_id'])

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)

print(all_fruits)
print('vodka' in all_fruits)

internal_ids = (151, 234)
external_ids = (624, 451, 941)

all_ids = internal_ids + external_ids

print(all_ids)
print(all_ids.count(624))
print(all_ids.index(234))

post_ids = (151, 254)

post_ids_list = list(post_ids)
post_ids_list.append(351)
post_ids_tuple = tuple(post_ids_list)

print(post_ids_tuple)

my_nums = (10, 5, 100, 5, 5)

index_one = my_nums.index(5)
index_two = my_nums.index(5, index_one + 1)
index_three = my_nums.index(5, index_two + 1)

print(index_one, index_two, index_three)

my_list = list(my_nums)

my_list.append(7)

print(my_list)

my_nums = tuple(my_list)

print(my_nums)

my_tuple = tuple('abcd')

print(my_tuple)

my_tuple = tuple({'first': 1, 'second': 2})

print(my_tuple)
