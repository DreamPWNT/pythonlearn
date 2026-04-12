my_range = range(7)

print(type(my_range))
print(my_range)
print(list(my_range))
print(list(range(10, 20, 3)))
print(my_range[2])

for n in my_range:
    print(n)

my_range = range(5)

print(my_range)
print(type(my_range))
print(my_range[0])
print(my_range[-1])

for n in my_range:
    print(n)

print(my_range[0])

for n in range(8):
    print(n)

for n in range(2, 7):
    print(n)

for n in range(12, 25, 5):
    print(n)

print(list(range(12, 25, 5)))
print(tuple(range(12, 25, 5)))
print(set(range(12, 25, 5)))
print(dir(my_range))
print(my_range.start, my_range.stop, my_range.step)
print(my_range.index(3))
print(my_range.count(1))
