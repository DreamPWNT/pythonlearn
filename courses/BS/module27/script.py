a = 10
b = a

c = a + b

print(a is b)
print(c is a)

a = [1, 2]
b = [1, 2]

print(a == b)
print(a.__eq__(b))
print(a.__eq__)
print(a is b)
print(id(a) == id(b), id(a), id(b), hex(id(a)), hex(id(b)))

my_num = 10

print(+my_num)
print(-my_num)

my_num = 10

print(not my_num)

my_car = {
    'brand': 'Toyota',
    'price': 10_000
}

print('brand' in my_car)
print('year' in my_car)
print('year' not in my_car)
