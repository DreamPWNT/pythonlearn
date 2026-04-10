my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_volume': 1.2
}

print(my_motorbike['brand'])
print(my_motorbike['price'])

my_motorbike['price'] = 20000

print(my_motorbike)
print(dir(my_motorbike))

my_motorbike['is_new'] = True

print(my_motorbike)

del my_motorbike['engine_volume']

print(my_motorbike)

key_name = 'brand'

my_motorbike[key_name] = 'BMW'

print(my_motorbike)

my_motorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 25000,
        'is_available': True
    }
}

print(my_motorbike['price_info']['price'])
print(my_motorbike['price_info']['is_available'])
print(len(my_motorbike))

del (my_motorbike['price_info'])

print(len(my_motorbike))
print(my_motorbike.get('model', 'S200'))
print(my_motorbike.get('price_info'))
print(my_motorbike.get('brand'))

my_dict = {}

print(my_dict.__doc__)
print(dict([(1, 2), (3, 4)]))

my_disk = {}

print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk)
print(id(my_disk))

print(my_disk.__doc__)
print("\n")
print(my_disk.items())
print(type(my_disk.items()))
print(my_disk.keys())
print(list(my_disk.keys()))
print(my_disk.popitem())
print(my_disk)

my_disk['price'] = 100

print(my_disk.get('type', 'hdd'))

new_disk = my_disk.copy()

new_disk['type'] = 'SSD'

print(my_disk, new_disk)
print(len(my_disk), len(new_disk))

my_list = [['first', 0], ['second', True]]
my_dict = dict(my_list)

print(my_dict)
