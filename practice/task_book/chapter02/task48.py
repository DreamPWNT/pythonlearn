birth_date = input('Enter birth date (DD.MM): ')

birth_day = int(birth_date[0:2])
birth_month = int(birth_date[3:])

if (22 <= birth_day <= 31 and birth_month == 12) or (1 <= birth_day <= 19 and birth_month == 1):
    print('Your zodiac sign is capricorn')
elif (20 <= birth_day <= 31 and birth_month == 1) or (1 <= birth_day <= 18 and birth_month == 2):
    print('Your zodiac sign is aquarius')
elif (19 <= birth_day <= 28 and birth_month == 2) or (1 <= birth_day <= 20 and birth_month == 3):
    print('Your zodiac sign is pisces')
elif (21 <= birth_day <= 31 and birth_month == 3) or (1 <= birth_day <= 19 and birth_month == 4):
    print('Your zodiac sign is aries')
elif (20 <= birth_day <= 30 and birth_month == 4) or (1 <= birth_day <= 20 and birth_month == 5):
    print('Your zodiac sign is taurus')
elif (21 <= birth_day <= 31 and birth_month == 5) or (1 <= birth_day <= 20 and birth_month == 6):
    print('Your zodiac sign is gemini')
elif (21 <= birth_day <= 30 and birth_month == 6) or (1 <= birth_day <= 22 and birth_month == 7):
    print('Your zodiac sign is cancer')
elif (23 <= birth_day <= 31 and birth_month == 7) or (1 <= birth_day <= 22 and birth_month == 8):
    print('Your zodiac sign is leo')
elif (23 <= birth_day <= 31 and birth_month == 8) or (1 <= birth_day <= 22 and birth_month == 9):
    print('Your zodiac sign is virgo')
elif (23 <= birth_day <= 30 and birth_month == 9) or (1 <= birth_day <= 22 and birth_month == 10):
    print('Your zodiac sign is libra')
elif (23 <= birth_day <= 31 and birth_month == 10) or (1 <= birth_day <= 21 and birth_month == 11):
    print('Your zodiac sign is scorpio')
elif (22 <= birth_day <= 30 and birth_month == 11) or (1 <= birth_day <= 21 and birth_month == 12):
    print('Your zodiac sign is sagittarius')
else:
    print('Incorrect birth date format')
