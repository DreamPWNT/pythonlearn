wave_length = int(input('Enter wave length of color spectrum: '))

if 380 <= wave_length < 450:
    print('Violet')
elif 450 <= wave_length < 495:
    print('Blue')
elif 495 <= wave_length < 570:
    print('Green')
elif 570 <= wave_length < 590:
    print('Yellow')
elif 590 <= wave_length < 620:
    print('Orange')
elif 620 <= wave_length < 750:
    print('Red')
else:
    print('Incorrect wave length value')
