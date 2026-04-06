MPG_COEFFICIENT = 235.214583

mpg = int(input('Enter miles per galons volume: '))

litres = round(MPG_COEFFICIENT / mpg, 2)

print(f'Litres per kilometer volume = {litres}')
