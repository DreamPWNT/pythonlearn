import sys

title = "Learning " 'Python' " 6E"

print(title)
print('python\'s', "python\"s")

s = 'a\nb\tc'

print(s)
print(len(s))

s = 'a\0b\0c'

print(s)
print(len(s))

s = '\001\002\x03'

print(s)
print(len(s))

S = 'H\tA\nC\x00K'

print(S)
print(len(S))
print('\400')
print('C:\py\code')

path = r'C:\new\text.dat'

print(path)
print(len(path))

quip = '''Python strings
sure have
a lot of options'''

print(quip)
print(len('abc'))
print('abc' + 'def')
print('Py!' * 4)
print('-' * 80)

myjob = 'hacker'

for c in myjob:
    print(c, end=' ')

print('k' in myjob)
print('z' in myjob)
print('HACK' in 'abcHACKdef')

S = 'code'

print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'

print(S[1:10:2])
print(S[::2])
print(S[::-1])
print(S[5:1:-1])
print('code'[1:3])
print('code'[slice(1, 3)])
print('code'[::-1])
print('code'[slice(None, None, -1)])

print(sys.argv)
print(sys.argv[1:])

S = '62'
I = 1

print(int(S) + I)
print(S + str(I))

print(ord('h'))
print(chr(104))

for c in 'hack':
    print(c, ord(c))

S = '5'
S = chr(ord(S) + 1)

print(S)

S = chr(ord(S) + 1)

print(S)
print('hack' == 'hack', 'hact' > 'hack', 'hacker' > 'hack')

S = 'text'
S = S + 'ual!'

print(S)

S = S[:4] + ' processing' + S[-1]

print(S)

S = 'text'
S = S.replace('ex', 'hough')

print(S)

S = 'hack'
result = S.find('ac')

print(result)

S = 'textly!'

print(S[:4] + 'ful' + S[-1])
print(S.replace('ly', 'ful'))
print('--@--@--@--'.replace('@', 'PY', 2))

S = 'xxxxPYxxxxPYxxxx'
where = S.find('PY')

print(where)

S = S[:where] + 'CODE' + S[(where + 2):]

print(S)

S = 'xxxxPYxxxxPYxxxx'

print(S.replace('PY', 'CODE', 1))
print(S.replace('PY', 'CODE'))
print('xxxxWHATxxxxHOWxxxx'.replace('WHAT', 'CODE').replace('HOW', 'PYTHON'))

S = S.replace('PY', 'CODE')

print(S)

S = 'text'
L = list(S)

print(L)

L[0] = 'h'
L[3] = '!'

print(L)

S = ''.join(L)

print(S)
print('PY'.join(['which', 'language', 'is', 'best', '?']))

line = 'aaa bbb ccc'

col1 = line[:3]
col2 = line[4:8]
col3 = line[-3:]

print(col1, col2, col3)

line = 'aaa bbb     ccc'

cols = line.split()

print(cols)

line = 'Python,3.12,scripting,33'

print(line.split(','))

line = 'youPYarePYaPYstringPYcoder'

print(line.split('PY'))

line = "Python's strings are awesome!\n"

print(line)
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('awesome!\n'))
print(line.startswith('Python'))
print(line.find('awesome') != -1)
print('awesome' in line)

sub = 'awesome!\n'

print(line.endswith(sub))
print(line[-len(sub):] == sub)

print('There are %d ways to %s!' % (3, 'format'))

option = 'expression'

print('Meet the formatting %s!' % option)
print('%d %s %g you' % (1, 'formatter', 4.0))
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))

x = 1234

res = 'integers: ...%d...%-6d...%06d' % (x, x, x)

print(res)

x = 1.23456789

print(x)
print('%e | %f | %g' % (x, x, x))
print('%E' % x)
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print('%s' % x, str(x))
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))
print('%(qty)s more %(tool)s' % {'qty': 1, 'tool': 'formatter'})

reply = '''
Hello %(name)s!
Welcome to %(year)s
'''
values = {'name': 'Pat', 'year': 2004}

print(reply % values)

name = 'Pat'
year = 2024

print(vars())
print('%(name)s from %(year)s' % vars())
print('%(value)f, %(value).2f, %(value).f' % ({'value': 1/3.0}))

template = '{}, {}, and {}'

print(template.format('expr', 'method', 'fstring'))

template = '{0}, {1}, and {2}'

print(template.format('expr', 'method', 'fstring'))

template = '{first}, {second}, and {third}'

print(template.format(first='expr', second='method', third='fstring'))

template = '{first}, {0}, and {third}'

print(template.format('method', first='expr', third='fstring'))

template = '%s, %s, and %s'

print(template % ('expr', 'method', 'fstring'))

template = '%(first)s, %(second)s, and %(third)s'

print(template % dict(first='expr', second='method', third='fstring'))
print('{pi}, {} and {years}'.format(62, pi=3.14, years=[1995, 2024]))

X = '{pi}, {} and {years}'.format(62, pi=3.14, years=[1995, 2024])

print(X)
print(X.split(' and '))

Y = X.replace('and', 'but under no circumstances')

print(Y)
print('This {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

somelist = list('HACK')

print(somelist)
print('zero={0[0]}, two={0[2]}'.format(somelist))
print('first={}, last={}'.format(somelist[0], somelist[-1]))
print(type(somelist[1:3]))
parts = (somelist[0], somelist[-1], ", ".join(somelist[1:3]))

print('first={}, last={}, middle={}.'.format(*parts))
print('{0:10} = {1:10}'.format('text', 123.4567))
print('{0:>10} = {1:<10}'.format('text', 123.4567))
print('{1[kind]:^10} = {0.platform:^10}'.format(sys, dict(kind='darwin')))
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('{:X}, {:o}, {:b}'.format(255, 255, 255))
print(hex(255), int('FF', 16), 0xFF)
print(oct(255), int('377', 8), 0o377)
print(bin(255), int('11111111', 2), 0b11111111)
print('{:,.2f}'.format(12345.678))
print('{0:,} {0:_} {1:_x} {1:_b}'.format(2 ** 32, 0x1FFFF))
print('{:.4f}'.format(1 / 3.0))
print('%.4f' % (1 / 3.0))
print('{0:.{1}f}'.format(1 / 3.0, 4))
print('%.*f' % (4, 1 / 3.0))
print('{:.2f}'.format(1.2345))
print(format(1.2345, '.2f'))
print('%.2f' % 1.2345)
print(f'{1.2345:.2f}')

what = 'coding'
tool = 'Python'

print(f'Learning {what} in {tool}')
print('Learning %s in %s' % (what, tool))
print('Learning {} in {}'.format(what, tool))

task = f'Learning {what.upper() + '!'} in {tool + str(3.12)}'

print(task)

what = 'f-strings'
task = f'Learning {what.upper() + '!'} in {tool + ' ' + str(3.14)}'

print(task)
print(f'{'\n'.join([what] * 3) + '\x21'}')
print(f'Learning {
    what.upper() + '!'
} in {tool + str(3.12)}')

a = 3.14156
b = 1_234_567

print(f'{a} and {b}')
print(f'{a:.2f} and {b:09}')
print(f'{a * 1000:e} an {b:+012,}')
print(f'{a * 1000:,.2f} and {b:,}')
print(f'{b:_X} and {b:_o} and {b // 64:_b}')
print(f'{a=:e} and {b=:+012}')
print(f'{a + 1=:e} and {b * 2=:+012}')

c = 'h\xc4ck'

print(f'{c} and {c} and {c}')
print(f'{c!s} and {c!r} and {c!a}')
print(f'{str(c)} and {repr(c)} and {ascii(c)}')
print(f'{c=!s} and {c=!r} and {c=!a}')
print(f'{c=!s:8} and {repr(c)} and {c:0>8} and {repr(ascii(c))}')

width = 8

print(f'{a:.8f} and {c:0>8}')
print(f'{a:.{width}f} and {c:0>{width}}')
print(f'{a=:.{width}f} and {c * 2:0>{width * 3}}')

what = 1_234.564
a, b, c, d, e, f, g, h = 0, '<', '+', 12, ',', '.', 2, 'f'

print(f'{what:0<+12,.2f}!')
print(f'{what:{a}{b}{c}{d}{e}{f}{g}{h}}!')

values = dict(tool='Python', role='scripting')

print('Use %(tool)s for %(role)s.' % values)
print('Use {tool} for {role}.'.format(**values))
print('Use {0[tool]} for {0[role]}.'.format(values))
print(f'Use {values['tool']} for {values['role']}.')

tool = 'Python'
role = 'scripting'

print(f'Use {tool} for {role}.')
