import math
import statistics
import random
import decimal
from fractions import Fraction

print(40 + 3.14)
print(int(3.1415))
print(float(3))

a = 3
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 ** b)

print(b / 2 + a)
print(b / (2 + a))

print(a, b)
print(b // 2 + a)
print(b // (2 + a))
print(b // 2.0 + a)
print(b // (2.0 + a))

print(1.1 + 2.2)

num = 1.1 + 2.2

print(num)
print('%e' % num)
print('%.1f' % num)
print(f'{num:e}', f'{num:.1f}')

print(repr('hack'))
print(str('hack'))

print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 6

print(X < Y < Z)
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y and Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)
print(1 == 2 < 3)
print(True is False is True)
print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))
print(round(1.1 + 2.2, 1) == round(3.3, 1))
print(math.isclose(1.1 + 2.2, 3.3))

print(10 / 4)
print(10 / 4.0)
print(10 // 4)
print(10 // 4.0)
print(int(10 // 4.0))
print(10 % 3, 10 % 3.0)
print(divmod(10, 3))
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))
print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)

print(1j * 1)
print(2 + 1j * 3)
print((2 + 1j) * 3)

print(0x01, 0x10, 0xFF)
print(0o1, 0o20, 0o377)
print(0b1, 0b10000, 0b11111111)
print(0xFF, (15 * (16 ** 1) + 15 * (16 ** 0)))
print(0x2F, (2 * (16 * 1) + 15 * (16 ** 0)))
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))
print(oct(64), hex(64), bin(64))
print(64, 0o100, 0x40, 0b1000000)
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))
print('%o, %x, %#X' % (64, 255, 255))
print('{:o}, {:b}, {:x}, {:#X}'.format(64, 64, 255, 255))
print(f'{64:o}, {64:b}, {255:x}, {255:#X}')
print('%(i)o, %(j)x, %(j)#X' % dict(i=64, j=255))
print('{0:o}, {0:b}, {1:x}, {1:#X}'.format(64, 255))
print(f'{(i := 64):o}, {1:b}, {(i := 255):x}, {i:#X}')

X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF

print(X)
print(oct(X))
print(bin(X))

x = 1

print(x << 2)
print(x | 3)
print(x & 3)

X = 0b0001

print(X << 2)
print(bin(X << 2))
print(bin(X | 0b0011))
print(bin(X & 0b11))

X = 0xFF

print(bin(X))
print(X ^ 0b10101010)
print(bin(X ^ 0b10101010))
print(int('01010101', 2))
print(hex(85))

X = 99

print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)

print(9999999999999 == 9_999_999_999_999)
print(0xFFFFFFFF == 0xFF_FF_FF_FF)
print(0o777777777777 == 0o777_777_777_777)
print(0b1111111111111111 == 0b1111_1111_1111_1111)
print(3.141592653589793 == 3.141_592_653_589_793)
print(123456789.123456789 == 123_456_789.123_456_789)

x = 9_999_998

print(x)
print(x + 1)
print(f'{x:,} and {x:_}')
print(99_9)
print(1_23_456_7890)
print(9_9_9)
print(hex(0xf_ff_fff_f_f))
print(int('1_234_567'))
print(eval('1_234_567'))
print(float('1_2_34.567_8_90'))

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
print(abs(-72.0), sum((1, 2, 3, 4)))
print(min(3, 1, 2, 4), max(3, 1, 2, 4))
print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(int(2.567), int(-2.567))
print(round(2.567), round(2.567, 2), round(2567, -3))
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))
print(1 / 3.0, round(1 / 3.0, 2), f'{(1 / 3.0):.2f}')
print(math.sqrt(144))
print(144 ** .5)
print(pow(144, .5))
print(statistics.mean([1, 2, 4, 5, 7]))
print(statistics.median([1, 2, 4, 5, 7]))
print(random.random())
print(random.randint(1, 10))
print(random.choice(['Pizza', 'Tacos', 'Tikka', 'Lasagna']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']

print(suits)

random.shuffle(suits)

print(suits)

print(0.1 + 0.1 + 0.1 - 0.3)
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') +
      decimal. Decimal('0.1') - decimal.Decimal('0.3'))
print(decimal.Decimal('0.1') + decimal.Decimal('0.10') +
      decimal.Decimal('0.1000') - decimal.Decimal('0.3'))
print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4

print(decimal.Decimal(1) / decimal.Decimal(7))

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

a = 1 / 3
b = 4 / 6

print(a)
print(b)
print(a + b)
print(a - b)
print(a * b)
print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') +
      decimal. Decimal('0.1') - decimal.Decimal('0.3'))
print(1 / 3)
print(Fraction(1, 3))

decimal.getcontext().prec = 2

print(decimal.Decimal(1) / decimal.Decimal(3))
print((1 / 3) + (6 / 12))
print(Fraction(1, 3) + Fraction(6, 12))
print(decimal.Decimal(1 / 3) + decimal.Decimal(6 / 12))

x = set('abcde')
y = {99, 'b', 'y', 'd', 1.2}

print(x)
print(y)

z = set()

print(z)

z = set([1.2, 'a', 3, 1.2, 'a'])

print(z)
print({1, *'abc', *[1, 2, 3]})

x = set('abcd')
y = set('bdxy')

print(x, y)
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)
print(x < y, x > y)
print('d' in x)
print('d' in 'code', 2 in [1, 2, 3])

z = x.intersection(y)

print(z)

z.add('HACK')

print(z)

z.update(set(['X', 'Y']))

print(z)

z.remove('b')

print(z)

for item in set('abc'):
    print(item * 3)

S = set([1, 2, 3])

print(S | set([3, 4]))
print(S.union([3, 4]))
print(S)
print(S.intersection((1, 3, 5)))
print(S)
print(S.issubset(range(-5, 5)))

S = set([1, 2, 3])
S.intersection_update((1, 2, 5))

print(S)

S |= {1, 2, 4}

print(S)

S = {1.23}

print(S)

S.add((1, 2, 3))

print(S)
print(S | {(4, 5, 6), (1, 2, 3)})
print((1, 2, 3) in S)
print((1, 4, 3) in S)

S.add(frozenset('app'))

print(S)

print({x ** 2 for x in [1, 2, 3, 4]})
print({x for x in 'py3X'})
print({c * 4 for c in 'py3X'})
print({c * 4 for c in 'py4X' + 'py2X'})

S = {c * 4 for c in 'py3X'}

print(S | {'zzzz', 'XXXX'})
print(S & {'zzzz', 'XXXX'})

L = [1, 2, 1, 3, 2, 4, 5]

print(L)
print(set(L))
print(list(set(L)))
print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))
print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
print(set('abcdefg') - set('abdghij'))
print(set('code') - set(['t', 'o', 'e']))

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]

print(L1 == L2)
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))
print('code' == 'edoc', set('code') == set(
    'edoc'), sorted('code') == sorted('edoc'))

engineers = {'pat', 'ann', 'bob', 'sue'}
managers = {'sue', 'tom'}

print('pat' in engineers)
print(engineers & managers)
print(engineers | managers)
print(engineers - managers)
print(engineers > managers)
print({'sue', 'bob'} < engineers)
print((managers | engineers) > managers)
print(managers ^ engineers)

print(type(True))
print(isinstance(True, int))
print(True == 1)
print(True is 1)
print(True or False)
print(True + 4)
