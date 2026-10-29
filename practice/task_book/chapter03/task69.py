total = 0.00

age = input("Enter age of group participant: ")

while (age != ''):
    if int(age) <= 2:
        cost = 0.00
    elif int(age) > 2 and int(age) <= 12:
        cost = 14.00
    elif int(age) > 12 and int(age) <= 65:
        cost = 23.00
    elif int(age) > 65:
        cost = 18.00

    total += cost

    age = input()

print(f"Sum of tickets = {round(total, 2)}$")
