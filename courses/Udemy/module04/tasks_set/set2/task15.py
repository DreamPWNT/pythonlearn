dates = ["2027.09.25", "2027.10.14", "2027.03.01",
         "2027.12.29", "2027.09.11", "2027.05.06"]
new = []

for date in dates:
    if date >= '2027.09.01':
        new.append(date)

print(new)

new.clear()

for date in dates:
    date_list = list(map(int, date.split('.')))

    if date_list[0] >= 2027 and date_list[1] >= 9 and date_list[2] > 1:
        new.append(date)

print(new)
