prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discounts = []
discount_prices = []

for price in prices:
    discount_sum = round(price * 0.6, 2)

    discounts.append(discount_sum)
    discount_prices.append(round(price - discount_sum, 2))

    print(f"${price:<6}".replace(".", ","), end=' ')

print()

for discount in discounts:
    print(f"${discount:<6}".replace(".", ","), end=' ')

print()

for discount_price in discount_prices:
    print(f"${discount_price:<6}".replace(".", ","), end=' ')
