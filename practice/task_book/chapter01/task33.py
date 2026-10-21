n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

max_num = max(n1, n2, n3)
min_num = min(n1, n2, n3)
avg_num = n1 + n2 + n3 - max_num - min_num

print(
    f'Max number = {max_num}, Avg number = {avg_num}, Min number = {min_num}')
