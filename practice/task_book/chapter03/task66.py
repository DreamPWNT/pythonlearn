import math

result = []

print('Enter summ in float: ')

while (True):
    x = input()

    if x == '':
        print('Exit...')
        break
    else:
        result.append(float(x))

if len(result) > 0:
    result_sum = sum(result)
    remainder = (result_sum * 100) % 5

    if remainder < 2.5:
        real_result_sum = result_sum - remainder / 100
    else:
        real_result_sum = result_sum + 0.05 - remainder / 100

    print(f"Sum: {result_sum}, Round sum: {real_result_sum}")
else:
    print("Sum: 0.00, Round sum: 0.00")
