my_fruits = ['apple', 'banana', 'lime']
posts_ids = [151, 234, 762, 167]
user_inputs = [True, 'hi', ':)', 10.5]
other_fruits = ['banana', 'apple', 'lime']

print(my_fruits == other_fruits)

empty_list = []

print(len(empty_list))
print(len(my_fruits))
print(len(posts_ids))
print(len(user_inputs))
print(posts_ids[0])
print(posts_ids[1])
print(posts_ids[-1])

posts_ids[0] = 555
posts_ids[2] = 333

print(posts_ids)

del (user_inputs[1])

print(user_inputs)
print(len(user_inputs))

del (user_inputs[-1])

print(user_inputs)
print(len(user_inputs))

users = [
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
]

print(len(users))
print(users[1]['user_id'])

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]

print(all_fruits)

happy_smiles = []

happy_smiles.append(':)')
happy_smiles.append('=)')
happy_smiles.append('xD')
happy_smiles.append(';)')

print(happy_smiles)
print(len(happy_smiles))

inputs = [True, 'hi!', ';)', 10.5]

print(inputs)

inputs.pop()

print(inputs)

inputs.pop(0)

print(inputs)

removed_element = inputs.pop()

print(removed_element)
print(posts_ids)

posts_ids.sort()

print(posts_ids)

posts_ids.sort(reverse=True)

greetings = "Hello from Python"
greetings_list = list(greetings)

print(greetings)
print(greetings_list)

my_dict = {'a': 10, 'b': True}

print(my_dict)
print(list(my_dict))

ratings = [2.5, 5.0, 4.3, 3.7]

print(max(ratings))
print(min(ratings))
print(sum(ratings))

my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings

print(all_ratings)
print(all_ratings[:2])
print(all_ratings[1: -1])
print(all_ratings[-2::-1])

my_cars = ['BWM', 'Mercedes']
copied_cars = my_cars

print(my_cars, copied_cars)

copied_cars.append('Audi')

print(my_cars, copied_cars)
print(id(my_cars), id(copied_cars))

my_cars = ['BWM', 'Mercedes']
copied_cars = my_cars[:]

copied_cars.append('Audi')

print(my_cars, copied_cars)
print(id(my_cars), id(copied_cars))
print(id(my_cars.copy()))

L1 = ['a', 'b', 'c']
L2 = list(''.join(L1))

print(L1, L2, id(L1), id(L2))

my_nums = [10, 50, 0, 5, 5, 100]

print(type(my_nums))
print(dir(my_nums))
print(my_nums.count(5))

my_nums.append(25)

print(my_nums)

my_nums.insert(3, 333)

print(my_nums)

my_nums.clear()

print(my_nums)

my_nums = [10, 50, 0, 5, 5, 100]

my_nums.extend('abc')

print(my_nums)
