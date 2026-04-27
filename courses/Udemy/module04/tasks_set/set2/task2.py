numbers = [2, 5, 0, 8, 11, 14, 17, 0]
new = []

for num in numbers:
    if num % 2 == 0 and num != 0:
        new.append(num)

print(new)
