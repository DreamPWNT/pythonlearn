date = input('Enter date: ')

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])

is_leap_year = False

if (year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)) or year % 400 == 0:
    is_leap_year = True

if (((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day == 31) or ((month == 4 or month == 6 or month == 9 or month == 11) and day == 30)):
    next_day = 1
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
elif month == 2:
    if is_leap_year and day == 29 or not is_leap_year and day == 28:
        next_day = 1
        next_month = month + 1
    else:
        next_day = day + 1
        next_month = month
    next_year = year
else:
    next_day = day + 1
    next_month = month
    next_year = year

print(f'+1 day is {next_day:02d}.{next_month:02d}.{next_year}')
