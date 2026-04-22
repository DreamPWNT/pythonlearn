for el in [1, 'abc', True]:
    print(type(el))
    print(el)

print(el)

print(dir())

my_dict = {'id': 324, 'title': 'test'}

for key in my_dict:
    print(type(key))
    print(key)
    print(my_dict[key])

my_object = {
    'x': 10,
    'y': True
}

for key, value in my_object.items():
    print(key, value)

video_ids = {1435, 4317, 2761, 5721}

for id in video_ids:
    print(id)

my_name = 'Vasisualiy'

for char in my_name:
    print(char)

for num in range(5):
    print(num)

for odd_num in range(3, 10, 2):
    print(odd_num)
my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(elem)

video_info = ('1920x1080', True, 27)

for elem in video_info:
    print(elem)

my_object = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_object:
    print(key, my_object[key])

for el in [1, 'abc', True]:
    print(type(el))
    print(el)

my_dict = {'id': 34, 'title': 'test'}

for key in my_dict:
    print(type(key))
    print(key)
    print(my_dict[key])

my_object = {
    'x': 10,
    'y': True
}

for item in my_object.items():
    key, value = item

    print(repr((key, value)))
