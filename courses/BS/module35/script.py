my_number = 25

if my_number > 0:
    print(my_number, 'is positive number')

person_info = {
    'age': 20
}

if not person_info.get('name'):
    print('Name is absent!')

if 10 > 2:
    print(True)

num_one = 10
num_two = 5

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_two, int)):

    print('Both numbers are ints ant positive')

my_number = 21.5

if type(my_number) is int:
    print(my_number, 'is integer')
else:
    print(my_number, 'is not an integer')

my_phone = {
    'price': 200,
    'brand': 'HTC'
}

if my_phone.get('brand'):
    print('Phone\'s brand is', my_phone['brand'])
else:
    print('There is no phone brand')

my_number = -10

if my_number > 0:
    print(my_number, 'is positive number')
elif my_number < 0:
    print(my_number, 'is negative number')
else:
    print(my_number, 'is zero')


def nums_info(a, b):
    if type(a) is not int or type(b) is not int:
        return 'One of arguments is not integer'

    if a >= b:
        return f'{a} >= {b}'

    return f'{a} < b'


print(nums_info(True, 4))
print(nums_info(10, 4))
print(nums_info(1, 4))
