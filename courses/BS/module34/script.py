my_fruits = ['apple', 'banana', 'lime']

my_apple, my_banana, my_lime = my_fruits

print(my_apple)
print(my_banana)
print(my_lime)

my_apple, *remaining_foods = my_fruits

print(my_apple)
print(remaining_foods)
print(type(remaining_foods))

user_profile = {
    'name': 'Vasisualiy',
    'comments_qty': 23
}


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f'User {name} has no comments...'
    else:
        return f'User {name} has {comments_qty} comments'


print(user_info(**user_profile))

name, comments_qty = user_profile

print(name, comments_qty)
print(user_profile.values())

user_data = ['Vasisualiy', 23]


def user_info(name, comments_qty=0):
    if not comments_qty:
        return f'User {name} has no comments...'
    else:
        return f'User {name} has {comments_qty} comments'


print(user_info(*user_data))

user_data = ('Vasisualiy', 23)

print(user_info(*user_data))

alco_list = [
    {'name': 'vodka', 'degrees': 40},
    {'name': 'cognac', 'degrees': 40},
    {'name': 'wine', 'degrees': 12}
]

vodka_info, cognac_info, wine_info = alco_list


def drink_info(name, degrees):
    print(f'Drink {name} consists {degrees} degrees of alcohol')


drink_info(**vodka_info)
drink_info(**cognac_info)
drink_info(**wine_info)
