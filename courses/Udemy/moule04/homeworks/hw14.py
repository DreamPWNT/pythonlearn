# Просьба не менять кортеж month тут.
month = (1, 2, 3, 4, 5, 6, 7,
         8, 9, 10, 11, 12, 13, 14,
         15, 16, 17, 18, 19, 20, 21,
         22, 23, 24, 25, 26, 27, 28,
         29, 30, 31)

week_days = ("Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday")
first = "Monday"  # День недели первого числа.

first_day_index = week_days.index(first)

counter = 0

while counter < 7:
    print(f'  {week_days[counter][0]}', end=('' if counter != 6 else '\n'))

    counter += 1

print()

counter = 0
day_index = first_day_index

while counter < len(month):
    if counter == 0:
        print('   ' * first_day_index, end='')

    if day_index == 6:
        print(f'{month[counter]:3}')

        day_index = 0
    else:
        print(f'{month[counter]:3}', end='', sep='')

        day_index += 1

    counter += 1
