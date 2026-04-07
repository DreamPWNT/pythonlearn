volume = int(input('Enter volume value: '))

if volume < 40 or volume > 130:
    print('Incorrect volume value')
elif volume == 40:
    print('Is quiet room')
elif 40 < volume < 70:
    print('Is quiet room or alarm clock')
elif volume == 70:
    print('Is alarm clock')
elif 70 < volume < 106:
    print('Is alarm clock or gas lawn mower')
elif volume == 106:
    print('Is gas lawn mower')
elif 106 < volume < 130:
    print('Is gas lawn mower or jackhammer')
elif volume == 130:
    print('Is jackhammer')
