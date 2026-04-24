temps = (12, 15, 14, 10, 9, 11, 13)  # кортежи одинаковой длины.
week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

count = 0

while count < len(temps):
    print(f'{week[count]}: {temps[count]:2d} °C')

    count += 1
