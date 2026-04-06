initial_sum = int(input('Enter initial deposit sum: '))

first_year_sum = initial_sum * 0.04 + initial_sum
second_year_sum = first_year_sum * 0.04 + first_year_sum
third_year_sum = second_year_sum * 0.04 + second_year_sum

print(f'Sum at the end of first year = {round(first_year_sum, 2)}')
print(f'Sum at the end of second year = {round(second_year_sum, 2)}')
print(f'Sum at the end of third year = {round(third_year_sum, 2)}')
