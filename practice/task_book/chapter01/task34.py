COST_CONSTANT = 3.49
DISCOUNT = 0.6

n = int(input('Enter quantity of yesterday breads: '))

cost_one = round(COST_CONSTANT * DISCOUNT, 2)
cost = round(n * COST_CONSTANT * 0.6, 2)

print(f'Bread cost: {cost_one:>15}')
print(f'Yesterday discount: {DISCOUNT:>6}')
print(f'Yesterday cost: {cost:>12}')
