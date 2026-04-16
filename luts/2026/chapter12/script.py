if 1:
    print('true')

if not 1:
    print('true')
else:
    print('false')

os, mode = 'Windows', 'mobile'

if os in ['iOS', 'iPhoneIS']:
    print('macOs')
elif mode == 'mobile' and os != 'Windows':
    print('Linux')
else:
    print('unknown?')

os, mode = 'Android', 'mobile'

if mode == 'mobile':
    if os == 'Android':
        print('Linux')
    elif os != 'Windows':
        print('macOS')

choice = 'Windows'

print({
    'macos': 2001,
    'Linux': 1991,
    'Windows': 1985
}[choice])

if choice == 'macos':
    print(2001)
elif choice == 'Linux':
    print(1991)
elif choice == 'Windows':
    print(1985)
else:
    print('Bad choice')

branch = dict(macos=2001, Linux=1991, Windows=1985)

print(branch.get('Windows', 'Bad choice'))
print(branch.get('Solaris', 'Bad choice'))

choice = 'AmigaOS'

if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

choice = 'GEM'

try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

state = 'halt'

match state:
    case 'go':
        print('green')
    case 'stop':
        print('red')
    case _:
        print('yellow')

match state:
    case 'go' | 'proceed' | 'start':
        print('green')
    case 'stop' | 'halt' as what:
        print('red')
        print('means', what)
    case other:
        print('catchall', other)

for stmt in ['if', 'while', 'try']:
    match stmt:
        case 'if' | 'match':
            print('logic')
        case 'for' | 'while' as which:
            print('loop')
        case other:
            print('tdb')

print(which, other)

state = dict(a=0, values=[1, 2, 3], tr=False, name='Vasisualiy')

print('\n\n')

match state:
    case 1 | 2 | 3 as what:
        print('or', what)
    case [1, 2, what]:
        print('list', what)
    case [0, *what]:
        print('list', what)
    case {'a': 1, 'b': 2, 'c': what}:
        print('dict', what)
    case {'a': 0, **what}:
        print('dict', what)
    case (2, 3, what):
        print('tuple, what')
    case (0, *what):
        print('tuple', what)
    case _ as what:
        print('other', what)


class Emp:
    def __init__(self, name): self.name = name


pat = Emp('Pat')                         # pat.name becomes 'Pat': see Part VI!

state = pat

match state:
    case pat.name as what:               # Match object's attribute, what = 'Pat'
        print('attr', what)
    case Emp(name=what):                 # Match an Emp instance, what = 'Pat'
        print('instance', what)

tone = 'formal'

a = 'code' if tone == 'formal' else 'hack'

print(tone, a)

L = [1, 0, 2, 0, 'hack', '', 'py', []]

print(list(filter(bool, L)))
