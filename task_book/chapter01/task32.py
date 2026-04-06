n = int(input('Enter 4-digital number: '))

first_digit = n // 1000
remainder = n % 1000
second_digit = remainder // 100
remainder = remainder % 100
third_digit = remainder // 10
fourth_digit = remainder % 10

digit_sum = first_digit + second_digit + third_digit + fourth_digit

print(f'Digit sum = {digit_sum}')
