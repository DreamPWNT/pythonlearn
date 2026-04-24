currencies = ("USD", "EUR", "GBP", "JPY", "CNY")
rates = (93, 101, 115, 0.63, 12.8)

count = 0

while count < len(currencies):
    print(f'{currencies[count]} | {rates[count]:6.2f}')

    count += 1
