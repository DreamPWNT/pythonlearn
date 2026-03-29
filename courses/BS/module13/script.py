is_authorized = True

print(is_authorized)
print(type(is_authorized))
print(100 > 24)
print(-5 > 0)
print('Long string' > 'Long')
print([1, 2, 3] == [1, 2, 3])

db_is_available = False

print(db_is_available)
print(type(db_is_available))

db_is_available = True

print(db_is_available)

print("Results!")
print(bool(10))
print(bool('abc'))
print(bool([]))
print(bool({}))
print(bool([1, 2, 3]))
print(bool(None))
print(100 > 10)
print('Long string' > 'long')
print([1] == [1])
print({'b': 1, 'a': 3} == {'a': 3, 'b': 1})
print(5 + 4.5)
print(4.5 + 5)

int_num = 50
float_num = 7.5
str_val = 'abc'

print(int_num + float_num)
print(int_num * float_num)
print(int_num.__add__(float_num))
print(int_num.__mul__(float_num))
print(float_num.__add__(int_num))
print(float_num.__mul__(int_num))
print(float_num.__radd__(int_num))
print(float_num.__rmul__(int_num))
print(int_num * str_val)
print(str_val * int_num)
print(int_num.__mul__(str_val))
print(str_val.__mul__(int_num))
print(str_val.__rmul__(int_num))

print(bool)
print(dir(bool))
print(dir(bool(10)))
print(bool.__doc__)
print(str.__doc__)

my_list = []

print(help(my_list.__eq__))
