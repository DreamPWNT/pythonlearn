less_litr = 0.1
more_litr = 0.24
less_litr_quantity = int(
    input("Enter quantity of bottles with volume 1 litr or less: "))
more_litr_quantity = int(
    input("Enter quantity of bottles with volume more 1 litr: "))

result = less_litr*less_litr_quantity + more_litr*more_litr_quantity

print(f'Cost of empty bottles = ${round(result, 2)}')
