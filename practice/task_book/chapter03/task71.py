approaches_quantity = 15
pi_value = 3
start_value = 2

for i in range(0, approaches_quantity):
    if not i % 2:
        pi_value += 4 / (start_value * (start_value + 1) * (start_value + 2))
    else:
        pi_value -= 4 / (start_value * (start_value + 1) * (start_value + 2))
    print(f"i = {i}, Pi = {pi_value}")
    start_value = start_value + 2

print(f"Pi = {pi_value}")
