day = int(input('Enter holiday day: '))
month = input('Enter holiday month name: ')

if day == 1 and month == 'january':
    print('Happy new year!')
elif day == 1 and month == 'july':
    print('Happy Canada\'s day!')
elif day == 25 and month == 'december':
    print('Merry Christmas!')
else:
    print('Ordinary day')
