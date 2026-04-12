print(len([1, 2, 3]))
print([1, 2, 3]+[4, 5, 6])
print(['Py!'] * 4)
print(str([1, 2]) + '34')
print([1, 2] + list('34'))

L = [1, [2, 3], 4]

print(L == [1, [2, 3], 4], L > [1, [2, 2], [4]], L > [1])

L = ['hack', 'Hack', 'HACK!']

print(L[2], L[-2], L[1:])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])

L = ['code', 'Code', 'CODE!']

L[1] = 'Hack'

print(L)

L[0:2] = ['write', 'Python']

print(L)

L = [1, 2, 3]

L[1:2] = [4, 5]

print(L)

L[1:1] = [6, 7]

print(L)

L[1:2] = []

print(L)

L = [1]

L[:0] = [2, 3, 4]

print(L)

L[len(L):] = [5, 6, 7]
L.extend([8, 9, 10])

print(L)

L = ['write']

L.append('Python')

print(L)

L.extend(['code', 'goodly'])

print(L)

L.sort()

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort()

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower, reverse=True)

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower)

print(L)

L = [1, 'hack', 2]

L.sort(key=str)

print(L)

L = ['abc', 'ABD', 'aBe']

print(sorted(L))
print(sorted(L, key=str.lower, reverse=True))
print(sorted([x.lower() for x in L], reverse=True))

L = [1, 2, 3, 4, 5]

print(L)
print(L.pop())
print(L)

L.reverse()

print(L)
print(list(reversed(L)))

L = []

L.append(1)
L.append(2)

print(L)

L.pop()

print(L)

L = ['hack', 'Py', 'code']

print(L.index('Py'))

L.insert(1, 'more')

print(L)

L.remove('code')

print(L)

L.pop(1)

print(L)
print(L.count('Py'))

print(3 in [1, 2, 3])

for x in [1, 2, 3]:
    print(x, end=' ')

print(list(range(5)))

res = [x * 4 for x in 'code']

print(res)

res = []

for x in 'code':
    res.append(x * 4)

print(res)

print([x * 4 for x in 'program' if x >= 'p'])
print([x + y for x in 'py' for y in '312'])
print(list(map(abs, [-1, -2, 0, 1, 2])))

L = ['code', 'hack']

print([L, 2, 3, L])
print([*L, 2, 3, *L])

S = 'coe'

print([*'Py', *S, *range(3)])
print(L + [2, 3] + L)
print(list('Py') + list(S) + list(range(3)))

M = []

for x in ('Py', S, range(3)):
    M.extend(x)

L = ['hack', 'more', 'Py', 'code']

del (L[0])

print(L)

del (L[1:])

print(L)

L = ['hack', 'more', 'Py', 'coded']

L[0:1] = []

print(L)

L[1:] = []

print(L)

L[0] = []

print(L)

D = {'hack': 1, 'Py': 2, 'code': 3}

print(D['Py'])
print(D)
print(len(D))
print('code' in D)
print(list(D.keys()))
print(D.keys())
print(D)

D['Py'] = ['app', 'dev']

print(D)

del (D['code'])

print(D)

D['years'] = 32

print(D)

D['Py'][0] = 'program'

print(D)

D = {'program': 1, 'script': 2, 'app': 3}

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))
print(D.get('script'))
print(D.get('code'))
print(D.get('code', 4))
print(D)

D2 = {'code': 4, 'hack': 5, 'app': 6}

print(D2)

D.update(D2)

print(D)
print(D.pop('app'))
print(D.pop('hack'))
print(D)

L = ['aa', 'bb', 'cc', 'dd']

print(L.pop())
print(L.pop(1))
print(L)

D = {}

D['name'] = 'Pat'
D['age'] = 40

print(D)
print(dict(name='Pat', age=40))
print(dict([('name', 'Pat'), ('age', 40)]))
print(dict.fromkeys(['a', 'b'], 0))

D = dict(a=4, c=3)

print({'a': 1, 'b': 2, **D})
print(dict(a=1, b=2) | D)
print(dict(a=1, **{'b': 2}, **dict(c=3)))
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
print(dict(zip(['a', 'b', 'c'], [1, 2, 3])))

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}

print(D)

D = {x: x ** 2 for x in [1, 2, 3, 4]}

print(D)

D = {c: c * 4 for c in 'HACK'}

print(D)

D = {c.lower(): (c + '!')for c in ['HACK', 'PY', 'CODE']}

print(D)

D = dict.fromkeys(['a', 'b', 'c'], 0)

print(D)

D = {k: 0 for k in ['a', 'b', 'c']}

print(D)

D = dict.fromkeys('code')

print(D)

D = {k: None for k in 'code'}

print(D)

D = dict(a=1, b=2)

D['c'] = 3

print(D)
print(D.pop('b'))
print(D)

D['b'] = 2

print(D)

D['c'] = 0
D['d'] = 1

print(D)
print(D.popitem())
print(D.popitem())
print(D)

D = dict(a=1, b=2)

print(D)
print(D | {'b': 3, 'c': 4})
print(D | {'b': 3, 'c': 4} | dict(a=4, d=6))

D = dict(a=1, b=2)

print(D)

C = D.copy()

C.update({'b': 3, 'c': 4})
C.update(dict(a=5, d=6))

print(C)

D = dict(a=1, b=2)

print(D)
print({**D, **{'b': 3, 'c': 4}, **dict(a=5, d=6)})

D1 = dict(a=1, b=1)
D2 = dict(a=2, c=2)

for k in D2:
    D1[k] = D2[k]

print(D1)

table = {
    '2024': 'Learning Python, 6th Edition',
    '2013': 'Learning Python, 5th Edition',
    '1999': 'Learning Python'
}

print(table['2024'])

for year in table:
    print(year + '\t' + table[year])

table = {
    'Learning Python, 6th Edition': 2024,
    'Learning Python, 5th Edition': 2013,
    'Learning Python': 1999
}

print(list(table.items())[:2])
print([title for (title, year) in table.items() if year == 1999])

K = 'Learning Python'
V = 1999

print(table[K])
print([key for (key, value) in table.items() if value == V])
print([key for key in table.keys() if table[key] == V])
print(dict(zip(table.values(), table.keys()))[1999])

D = {}

D[99] = 'hack'

print(D)

D[62] = 'code'
D[30] = 'write'

print(D[62])
print(D)

Matrix = {}

Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2
Y = 3
Z = 4

print(Matrix[(X, Y, Z)])
print(Matrix)
print(Matrix.get((2, 3, 4), 0))
print(Matrix.get((2, 3, 6), 0))

if (2, 3, 6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

rec = {}

rec['title'] = 'Learning Python, 5th Edition'
rec['year'] = 2013
rec['isbn'] = '9871449355739'

print(rec['year'], rec['isbn'])

rec = {
    'title': 'Learning Python, 5th Edition',
    'date': {
        'year': 2013,
        'month': 'July'
    },
    'isbns': ['1449355730', '9781449355739']
}

print(rec['title'])
print(rec['isbns'])
print(rec['isbns'][1])
print(rec['date']['year'])

D = dict(program=1, script=2, app=3)

print(D.keys())

D = dict(a=1, b=2, c=3)

print(D)

K = D.keys()

print(K)
print(list(K))

V = D.values()

print(V)
print(list(V))
print(D.items())
print(list(D.items()))
print(list(K)[0], list(K).sort())

D = {'a': 1, 'b': 2, 'c': 3}

print(D)

K = D.keys()
V = D.values()

print(list(K), list(V))

del D['b']

print(list(K), list(V))
print(K, V)
print(K | {'x': 4})

D = {'a': 1, 'b': 2, 'c': 3}

print(D.keys() & D.keys())
print(D.keys() & {'b'})
print(D.keys() & {'b': 1})
print(D.keys() | {'b', 'c', 'd'})

D = {'a': 1}

print(D.items())
print(D.items() | D.keys())
print(D.items() | D)
print(dict(D.items() | {('c', 3), ('d', 4)}))

D = {'c': 3, 'b': 2, 'a': 1}

print(D)

Ks = list(D.keys())
Ks.sort()

for k in Ks:
    print(k, D[k])

Ks = D.keys()

for k in sorted(Ks):
    print(k, D[k])

print(sorted(D))

D1 = dict(a=1, b=2, c=3)
D2 = dict(c=3, b=2, a=1)

print(D1 == D2, D1 != D2)

D1 = dict(a=1, b=2, c=4)
D2 = dict(c=3, b=2, a=1)

print(list(D1.items()), list(D2.items()))
print(D1.items() > D2.items())
print(sorted(D1.items()) > sorted(D2.items()))

D = {}

D['state1'] = True

print('state1' in D)

S = set()

S.add('state1')

print('state1' in S)
