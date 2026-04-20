S1 = {1, 2, 3}
S2 = {3, 2, 1}

print(S1 == S2)
print(S1 is S2)
print(1 in S1)
print(3 in S2)
print(33 in S2)
print(13 in S1)

a, b, c = 1, 2, 3

S1 = {a, b, c}
S2 = {a, b, c}

print(S1 is S2)

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print(bool(''))
print(not not {'a': 1})
print(not not {})

my_list = [1, 2]

if len(my_list) > 0:
    print('List has elements')
