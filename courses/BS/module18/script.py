my_fruits = {'apple', 'banana', 'lime'}
posts_ids = {151, 245, 762, 167}
user_inputs = {True, 'hi!', ':)', 10.5}

print(my_fruits)
print(type(my_fruits))

other_fruits = {'banana', 'apple', 'lime'}

print(my_fruits == other_fruits)

post_ids = {10, 25, 16, 37}

my_set = {10, 10, 5, 15, 15}

print(my_set)
print(len(my_set))

my_set = {(10, 10), 5, 15, 15}

print(my_set)
print(set())
print(type(set()))

photo_sizes = {'1920x1080', '800x600'}

photo_sizes.add('1024x768')

print(photo_sizes)

photo_sizes = {'1920x1080', '800x600'}
other_sizes = {'800x600', '1024x768'}
other_sizes_2 = {'800x600'}

print(photo_sizes.union(other_sizes))
print(photo_sizes | other_sizes)
print(photo_sizes.intersection(other_sizes))
print(photo_sizes & other_sizes)
print(other_sizes_2.issubset(photo_sizes))
print(photo_sizes.issuperset(other_sizes_2))

my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))
print(other_set.intersection(my_set))
print(my_set.union(other_set))
print(other_set.issubset(my_set))
print(my_set.issuperset(other_set))
print(my_set.difference(other_set))
print(my_set - other_set)
print(my_set.remove('d'))

copied_set = my_set.copy()

print(copied_set)
print(my_set & copied_set)
print(my_set.symmetric_difference(other_set))
print(my_set ^ other_set)
print(my_set & copied_set - other_set)
