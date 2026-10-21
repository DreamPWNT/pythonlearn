summa = float(input("Enter order sum: "))

tax = round(summa * 0.13, 2)
tips = round(summa * 0.18, 2)
charge = tax + tips

print(
    f'Tax = {round(tax, 2)}, Tips = {round(tips, 2)}, Total charge = {round(charge, 2)}')
