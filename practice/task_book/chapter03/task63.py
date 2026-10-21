result = []

print('Enter numbers (0 to exit):')

while True:
    x = int(input())

    if (x == 0):
        if len(result) == 0:
            print('Error, first number is zero. Exit...')
        break
    else:
        result.append(x)

print(
    f'Average value of input numbers = {(sum(result) / len(result)) if x != 0 else 'undefined'}')
