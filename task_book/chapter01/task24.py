

days = int(input('Enter days quantity: '))
hours = int(input('Enter hours quantity: '))
minutes = int(input('Enter minutes quantity: '))
seconds = int(input('Enter seconds quantity: '))

full_second_time = seconds + minutes * 60 + hours * 3600 + days * 86400

print(f'Full time in seconds = {full_second_time}')
