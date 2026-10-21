weight = int(input('Enter your weight in kilograms: '))
height = int(input('Enter your height in centimeters: '))

BMI = weight / pow(height, 2)

print(f'Your BMI = {BMI}')
