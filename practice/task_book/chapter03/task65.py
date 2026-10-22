print(f'Celcium | Farenheit')

for degree in range(101):
    if not degree % 10:
        print(f"{degree:<7} | {int(degree * 1.8 + 32):<7}")
