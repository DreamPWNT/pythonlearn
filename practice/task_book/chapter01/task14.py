foots = int(input('Enter height in foots: '))
inches = int(input('Enter height in inches: '))

height_sm = (foots*12 + inches) * 2.54

print(f'Height is centimeters = {height_sm}')
