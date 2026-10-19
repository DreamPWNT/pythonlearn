res = []

for x in 'text':
    res.append(ord(x))

print(res)
print(list(map(ord, 'text')))
print([ord(x) for x in 'text'])
print([x ** 2 for x in range(10)])
print(list(map(lambda x: x ** 2, range(10))))
print([x for x in range(10) if x % 2 == 0])
print(list(filter(lambda x: x % 2 == 0, range(10))))

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]

print(res)
print([x + y for x in 'orm' if x in 'ro' for y in 'ORM' if y > 'M'])
print([
    x + y + z
    for x in 'hack' if x > 'c'
    for y in 'CODE' if y in 'OD'
    for z in '123' if z > '1'
])
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]]

print(M[1])
print(M[1][2])
print([row[1] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print(len(M))
print([M[i][i] for i in range(len(M))])
print([M[i][len(M)-1-i] for i in range(len(M))])

L = [[1, 2, 3], [4, 5, 6]]

print([col + 10 for row in M for col in row])
print([[col + 10 for col in row] for row in M])

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for col in range(len(M))]
      for row in range(len(M))])


def genquares(n):
    for i in range(n):
        yield i ** 2


for i in genquares(5):
    print(i, end=' ')

print()

x = genquares(3)

print(x)
print(next(x))
print(next(x))
print(next(x))


def ups(line):
    for sub in line.split(','):
        yield sub.upper()


print(tuple(ups('aaa,bbb,ccc')))
print({i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))})


def gen():
    for i in range(10):
        X = yield i
        print('=>', X)


G = gen()

print(next(G))
print(G.send(12))
print(G.send(12432))
print(G.send(1235634567342))
print(G.send(12342342))
print(next(G))


def both(N):
    yield from range(N)
    yield from map(lambda x: x ** 2, range(N))


print(list(both(5)))

G = (c * 4 for c in 'hack')

print(list(G))


def timesfour(S):
    for c in S:
        yield c * 4


G = timesfour('hack')

print(list(G))

L = ['a', 'b', 'vodka', 'seledka']

print({x: s for (x, s) in zip(range(len(L)), L)})

L, S = [1, 2, 3], 'code'

for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=" ")

print()

for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=' ')

print()


def scramble(seq):
    res = []

    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])

    return res


print(scramble('code'))


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


print(scramble('code'))


def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


print(list(scramble('code')))
print(list(scramble((1, 2, 3, 4, 5))))

for x in scramble((1, 2, 3)):
    print(x, end=' ')

print()

print(list(zip('abc', 'xyz123')))
print(list(zip((1, 2, 3), [2, 3, 4, 5])))
print(list(zip([-2, -1, 0, 1, 2])))
print(list(map(abs, [-2, -1, 0, 1, 2])))
print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))


def my_map(func, *seqs):
    return (func(*args) for args in zip(*seqs))


print(list((my_map(abs, [-1, -2, -3]))))
print(list((my_map(pow, [-1, -2, -3], [9, 5, 2]))))
