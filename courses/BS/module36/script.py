my_number = 21.5

print('is int') if type(my_number) is int else print('is not int')

product_qty = 10

print('in stock' if product_qty > 0 else 'out of stock')

temp = +24

weather = 'hot' if temp > 18 else 'cold'

print(weather)

my_img = ('1920', '1080')

print(f'{my_img[0]}x{my_img[1]}' if len(my_img)
      == 2 else f'Incorrect image formatting')

if len(my_img) == 2:
    print(f'{my_img[0]}x{my_img[1]}')
else:
    print(f'Incorrect image formatting')
