denomination = int(input("Enter denomination of the banknote: "))

if denomination == 1:
    print('George Washington')
elif denomination == 2:
    print('Tomas Jefferson')
elif denomination == 5:
    print('Avraam Linkoln')
elif denomination == 10:
    print('Alexander Gamilton')
elif denomination == 20:
    print('Andrew Jackson')
elif denomination == 50:
    print('Ulysses Grant')
elif denomination == 100:
    print('Benjamin Franklin')
else:
    print('President not found!!!')
