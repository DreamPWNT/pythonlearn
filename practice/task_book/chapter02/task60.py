import math

year = int(input('Enter year: '))

day_of_week = (year + math.floor((year - 1) / 4) -
               math, math.floor((year - 1) / 100) + math.floor((year - 1) / 400)) % 7

if day_of_week == 0:
    print('1 January in {year} will be at Saturday')
elif day_of_week == 1:
    print('1 January in {year} will be at Monday')
elif day_of_week == 2:
    print('1 January in {year} will be at Tuesday')
elif day_of_week == 3:
    print('1 January in {year} will be at Wednesday')
elif day_of_week == 4:
    print('1 January in {year} will be at Thursday')
elif day_of_week == 5:
    print('1 January in {year} will be at Friday')
elif day_of_week == 6:
    print('1 January in {year} will be at Sunday')
