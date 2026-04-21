import random

i = 10

while i < 50:
    print(i)

    i += 10

while True:
    answer = input('Enter ys or no: ')

    if answer == 'no':
        break

random_num = random.randint(1, 5)

while True:
    num = int(input('Guess the number from 1 to 5: '))

    if num != random_num:
        print('Try again...')

        continue

    print('Congratulation!', random_num)

    break
