# 1.a

S = input('Enter any string: ')

for ch in S:
    print(f'{ch}={ord(ch)}', end=',')

# 1.b

sum = 0

for ch in S:
    sum += ord(ch)

print()
print(f'Sum of ord string = {sum}')

# 1.c

L = []

for ch in S:
    L.append(ord(ch))

print(L)
print(map(ord, S))
print(list(map(ord, S)))
print([ord(ch) for ch in S])

# 2
month = int(input('Enter month number: '))

if month == 1:
    print('January')
elif month == 2:
    print('February')
elif month == 3:
    print('March')
else:
    print('Incorrect month number!!!')

match month:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case _:
        print('Incorrect month number!!!')

# 4
D = {'c': 1, 'z': 5, 'a': 4544, 'c': 52, 'b': 999}

keys_list = sorted([key for key in D])
sorted_dict = {k: D[k] for k in keys_list}

print(sorted_dict)

# 5

L = []
X = 5

for x in range(0, 6):
    L.append(2 ** x)

found = False
i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i + 1

if found:
    print('at index', i)
else:
    print(X, 'not found')

i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)

        break
    else:
        i = i + 1
else:
    print(X, 'not found')

for el in L:
    if 2 ** X == el:
        print(f'at index {L.index(el)}')

        break
else:
    print(X, 'not found')

print(f'at index {L.index(2 ** X)}' if 2 ** X in L else f'{X} not found')
