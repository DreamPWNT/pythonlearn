import time

count = 0

while count < 5:
    print(count)

    count += 1

print(count)

# password = input('Create your password:\n')
#
# while True:
#    if len(password) < 8:
#        print('Password must be at least 8 characters long')
#
#        password = input('Enter your password again:\n')
#    else:
#        break
#
# print(password)

# user_input = input('Enter something:\n')
#
# vowels = 'eyuioa'
# vowels_count = 0
# index = 0
# a_count = 0
#
# while index < len(user_input):
# char = user_input[index]
# index += 1
#
# if char == 'a' and a_count > 0:
# continue
#
# if char in vowels:
# if char == 'a' and a_count > 0:
# continue
# if char == 'a':
# a_count += 1
#
# vowels_count += 1
# elif char == 't':
# break
# else:
# vowels_count += 1
#
# print(vowels_count)

palindrome = 'racecar'
is_palindrome = palindrome == palindrome[::-1]

print(is_palindrome)

i = 0
j = len(palindrome) - 1

is_palindrome = True

while i < j:
    if palindrome[i] != palindrome[j]:
        is_palindrome = False

        break

    i += 1
    j -= 1

print(is_palindrome)

data = (5, 6, 25, -256, 'cake', True)

print(data)
print(data[2])

index = 0

x = data[1:3]

print(x)

x = (1,)

print(x, type(x))

data = data + ('FAQ',)

print(data)

date = (3, 'December', 2025)

day, month, year = date

print(f'It\'s {month} {day} {year}.')

x = ()

print(type(x))

day, *other = (3, 'December', 2025)

print(day)
print(other)

day, *other = 'Hello'

print(day, other)

data = ('Home', 'Catalog', 'Peyment & Shipping', 'About')
appartments = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
               12, 13, 14, 15, 16, 17, 18, 19, 20)
vertabrae = ('C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'T1',
             'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12')

print(vertabrae.index('T2'))

C = 8
T = 12

new = vertabrae[vertabrae.index('T2'): C + T]

print(new)
print(''.join(vertabrae))
print(' - '.join(vertabrae))
print('-'.join(map(str, (2, 2, 2, 3, 4, 21,))))

numbers = list()

print(type(numbers))

data_tuple = (2, 4, 6, 8, 10)
data_list = [2, 4, 6, 8, 10]

print(id(data_list))

data_list[1] = 'Alice'

print(data_list)
print(data_list[0:2])
print(id(data_list))

data_list = data_list + [2, 1]

print(data_list)
print(id(data_list))

data_list_2 = data_list

data_list += [2]

print(data_list)
print(data_list_2)

prices = [5.24, 15.99, 100.25, 1.55, 17.15]
discount_prices = []

discount = 0.9
count = 0

while count < len(prices):
    discount_prices.append(round(prices[count] * discount, 2))
    prices[count] = round(prices[count] * discount, 2)

    count += 1

print(prices)
print(discount_prices)

prices = [5.25, 25.99, 100.25, 1.55, 17.15]
additional_prices = [5.15, 6.99]

prices += additional_prices

print(prices)

prices.extend(additional_prices)

print(prices)
print(prices.clear())
print(prices)

prices = [5.25, 15.99, 100.25, 1.55, 17.15]

print(prices)
print(prices.remove(15.99))
print(prices)
print(prices.pop())
print(prices.pop(0))
print(prices)

prices.sort()

print(prices)

prices.sort(reverse=True)

print(prices)

prices.reverse()

print(prices)

new = prices.copy()

prices[0] = 0

print(new)
print(prices)

s = 'Hello!'

new_s = s.lower().replace('!', '?')

prices.sort()

print(new_s)
