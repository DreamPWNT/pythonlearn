time = int(input('Enter time in seconds: '))

days = time // 86400
remainder = time % 86400
hours = remainder // 3600
remainder = remainder % 3600
minutes = remainder // 60
remainder = remainder % 60
seconds = remainder

print(f'Human time is {days}:{hours:02d}:{minutes:02d}:{seconds:02d}')
