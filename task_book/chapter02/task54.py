BONUS_CONST = 2400.00

rating = float(input(f'Enter employee rating: '))
bonus = False

if rating == 0.0:
    bonus = 0.0
elif rating == 0.4:
    bonus = 0.4 * BONUS_CONST
elif rating >= 0.6:
    bonus = 0.6 * BONUS_CONST

if (bonus != False or bonus == 0.0):
    print(f'Employee rating is: {rating}, employee bonus = {bonus}$')
else:
    print('Incorrect input')
