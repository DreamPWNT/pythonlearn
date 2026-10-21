pattern = 'aeiou'

s = input('Enter a symbol: ')

if s in pattern:
    print('Symbol is vowel')
elif s == 'y':
    print('Symbol may be vowel or consonant')
else:
    print('Symbol is consonant')
