import math

result = 2*(2 - 2) / 2

print(result)

cash = 11287

bill_100 = cash // 100
bill_50 = (cash % 100) // 50
bill_20 = ((cash % 100) % 50) // 20
bill_5 = (((cash % 100) % 50) % 20) // 5
bill_1 = (((cash % 100) % 50) % 20) % 5

print(bill_100, bill_50, bill_20, bill_5, bill_1)

x = 256 / 11
res = round(x, 1)

print(237 / 48)
print(res)
print(0.1 + 0.2)
print(round(0.1 + 0.2, 2))
print(f'{4.55:.20f}')
print(type(round(x)))
print(round(x))

res_2 = math.ceil(x)
print(res_2)

res_3 = math.floor(x)
print(res_3)

# enter = input("Enter something: ")
#
# print(enter)
# print(type(enter))

x = print('Hello')

print(x)
print(dir())
print(dir(__builtins__))

# entered_num = float(input("Enter the number for your choice: "))
#
# print(entered_num + 2)
# print(float("-2.256"))

character = 'A'

x = ord(character)

print(x)
print(chr(x))
print(ord('Я'))

character = "25"

n = (ord("2") - 48) * 10 + (ord("5") - 48)

print(n)

num = bool("")

print(num)

print(5 == 6)
print(5 >= 6)
print(5 > 4)
print(5 <= 5)
print(5 != 5)

x = 5

num = 2 + 2 > x

print(num)
print(2 < x < 10)
print(2 < x + 1 < 10)

url = 'www.google.com'
broken_url = 'wxw.google.com'

print('www.google.com' == url)
print(url == broken_url)
print(url > broken_url)
print(url < broken_url)
print('www' in url)
print('www' in broken_url)
print(not 5 > 5)
print('vasia' not in url)

x = 0

if x:
    print(100 / x)
else:
    print("Fucking division by zero!!!!! Cancer!!!")

print("Program finished!")

value = float(input("Value: "))
part = float(input("How many?: "))

if value <= 0 or part < 0:
    print("Fucking division by zero or negative values!!!!! Cancer!!!")
else:
    percent = part / value * 100

    print(round(percent, 2), '%')

x = -5
y = 7

if x >= 0 and y >= 0:
    print(x * y)

if x >= 0 or y >= 0:
    print(x * y)

num_tickets = 248
bus_capacity = 48

num_tickets_left = num_tickets % bus_capacity
bus_quantity = num_tickets // bus_capacity
has_partial_bus = False
empty_seats = 0

if num_tickets_left >= bus_capacity / 2:
    bus_quantity += 1
    has_partial_bus = True
    empty_seats = bus_capacity - num_tickets_left
    num_ticket_left = 0

print(bus_quantity, num_tickets_left, has_partial_bus, empty_seats)
