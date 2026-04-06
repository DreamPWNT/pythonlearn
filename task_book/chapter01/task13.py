change = int(input('Enter change value: '))

coins_2l_quantity = change // 200
remainder = change % 200
coins_1l_quantity = remainder // 100
remainder = remainder % 100
coins_25c_quantity = remainder // 25
remainder = remainder % 25
coins_10c_quantity = remainder // 10
remainder = remainder % 10
coins_5c_quantity = remainder // 5
remainder = remainder % 5
coins_1c_quantity = remainder

print(f'2l: {coins_2l_quantity}, 1l: {coins_1l_quantity}, 25c: {coins_25c_quantity}, 10c: {coins_10c_quantity}, 5c: {coins_5c_quantity}, 1c: {coins_1c_quantity}')
