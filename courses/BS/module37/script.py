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
