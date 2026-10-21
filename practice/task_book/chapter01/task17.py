SPECIFIC_HEAT_COEFFICIENT = 4.186
CUP_VOLUME = 200
KILOWATTS_COEFFICIENT = 3_600_000
KILOWATT_COST = 8.9

m = int(input('Enter water weight: '))
delta_t = int(input('Enter temperature delta: '))

q = m * SPECIFIC_HEAT_COEFFICIENT * delta_t
cost = CUP_VOLUME * q / KILOWATTS_COEFFICIENT * KILOWATT_COST

print(f'Heating of {m} grammes requires {q}J')
print(f'Cost of water cup = {cost}$')
