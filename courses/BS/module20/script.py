fruits = ['apple', 'banana', 'lime', 'orange']
quantities = [100, 70, 50, 20]
availability = [True, False, False, True]

fruit_qtys_zip = zip(fruits, quantities, availability)

print(fruit_qtys_zip)
print(type(fruit_qtys_zip))

fruit_qtys_list = list(fruit_qtys_zip)

print(fruit_qtys_list)

goods = ['sugar', 'bread', 'potatos']
prices = [65, 67, 35]

print(list(zip(goods, prices)))
print(dict(zip(goods, prices)))
