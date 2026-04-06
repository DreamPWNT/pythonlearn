INCHES_COEFFICIENT = 12
YARDS_COEFFICIENT = 0.33333
MILES_COEFFICIENT = 0.000189

foots = int(input('Enter distance in foots: '))

inches = foots * INCHES_COEFFICIENT
yards = round(foots * YARDS_COEFFICIENT, 2)
miles = round(foots * MILES_COEFFICIENT, 2)

print(f'Distance in inches = {inches}, in yards = {yards}, in miles = {miles}')
