frequency = int(input('Enter electro-magnetic waves frequency: '))

if frequency < 3 * pow(10, 9):
    print('Radio waves')
elif 3 * pow(10, 9) <= frequency <= 3 * pow(10, 12):
    print('Micro waves')
elif 3 * pow(10, 12) <= frequency <= 4.3 * pow(10, 14):
    print('Infrared waves')
elif 4.3 * pow(10, 14) <= frequency <= 7.5 * pow(10, 14):
    print('Visual waves')
elif 7.5 * pow(10, 14) <= frequency <= 3 * pow(10, 17):
    print('Ultra violet waves')
elif 3 * pow(10, 17) <= frequency <= 3 * pow(10, 19):
    print('X-Ray waves')
elif frequency >= 3 * pow(10, 19):
    print('Gamma waves')
else:
    print('Incorrect input!')
