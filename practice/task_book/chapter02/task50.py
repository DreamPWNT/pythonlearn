magnitude = float(input('Enter earthquake magnitude: '))

if 0 <= magnitude < 2.0:
    print('Minimal earthquake')
elif 2.0 <= magnitude < 3.0:
    print('Very weak earthquake')
elif 3.0 <= magnitude < 4.0:
    print('Weak earthquake')
elif 4.0 <= magnitude < 5.0:
    print('Intermediate earthquake')
elif 5.0 <= magnitude < 6.0:
    print('Moderate earthquake')
elif 6.0 <= magnitude < 7.0:
    print('Hard earthquake')
elif 7.0 <= magnitude < 8.0:
    print('Very hard earthquake')
elif 8.0 <= magnitude < 9.0:
    print('Huge earthquake')
elif 9.0 <= magnitude < 10.0:
    print('Destructive earthquake')
else:
    print('Incorrect magnitude value. Must be 0.0 - 10.0')
