month = input('Enter month name: ')
day = int(input('Enter day number: '))

if month == 'january' or month == 'february' or (month == 'december' and day >= 21) or (month == 'march' and day < 20):
    print('Is winter')
elif month == 'april' or month == 'may' or (month == 'march' and day >= 20) or (month == 'june' and day < 21):
    print('Is spring')
elif month == 'july' or month == 'august' or (month == 'june' and day >= 21) or (month == 'september' and day < 22):
    print('Is summer')
elif month == 'october' or month == 'november' or (month == 'september' and day >= 22) or (month == 'decemper' and day < 21):
    print('Is autumn')
else:
    print('Incorrect input!')
