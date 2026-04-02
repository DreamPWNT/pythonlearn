import math
import sys

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


# value = float(input("Value: "))
# part = float(input("How many?: "))
#
# if value <= 0 or part < 0:
# print("Fucking division by zero or negative values!!!!! Cancer!!!")
# else:
# percent = part / value * 100
#
# print(round(percent, 2), '%')

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

n = int()
s = str()

print(n)
print(s)
print(type(n))
print(type(s))

s = "AAA"
x = s.lower()

print(s)
print(x)

x = "AAA"
y = x

print(id(x))
print(id(y))
print(hex(id(x)))
print(hex(id(y)))

print(x is y)
print(x == y)

print(sys.getrefcount(y))

x = 5
y = 10

print(id(x))
print(id(y))
print(sys.getrefcount(x))
print(sys.getrefcount(y))

x = 50_000_000_000

print(x)

x = .25

print(x)

x = 0b1000001

print(x)

x = 255
y = 255.0

new_obj = y.is_integer()

print(new_obj)

if y.is_integer:
    y = int(y)

print(y)

user_input = 'Привет'

word = 'привет'

if word in user_input.lower():
    print("Yo bro!!!")

new = user_input.lower()

print(user_input)
print(new)

user_input = '/'

if user_input.startswith('/'):
    print("Right command!")

user_input = '2,55'

if ',' in user_input:
    user_input = user_input.replace(',', '.')

print(user_input)
print(user_input.count('2'))

user_input = 'heLlo'

print(user_input)

url = 'http://www.google.com'
right_url = url.replace('http:', 'https:', count=1)

print(url)
print(right_url)

print(url[0])
print(url[1])
print(url[-1])

index = len(url) - 1

print(url[index])

item = url[4]

part = url[0:4:2]

print(url)
print(part)
print(url[7:10:1])
print(url[:4])
print(url[7:])
print(url[:])
print(url[-21:21:])
print(url[21:4:-2])

start_index = url.index('www.') + 4
domain = url[start_index:]

print(domain)

vertebrae = "C1, C2, C3, C4, C5, C6, C7"
vertebrae2 = "C1, C2, C3, C4, C5, C6, C7"

print(id(vertebrae))
print(id(vertebrae2))

numbers_str = vertebrae[1::4]

print(numbers_str)
print(vertebrae[-5:1:-1])

ascii = 'a' * 10
not_only_ascii = 'a' * 9 + 'бб'

print(not_only_ascii.__sizeof__() - 'б'.__sizeof__())

x = 'Hello ' \
    'World!'

print(x)

x = '''
Hello
'''

print(x)

x = "Hello \nWorld!"

print(x)

name = 'Alex'
id = 123496789

message = 'Hello {}, your id is: {}'.format(name, id)
message = f'Hello {name}, your id is: {id}'

print(message)

rating = 4.951246

print(f'Hello {name}, your id is: {rating:.2f}')
print('Hello {}, your id is: {:.2f}'.format(name, rating))
print('Hello {name}, your id is: {rating:.2f}'.format(
    name=name, rating=rating))
print('Hello %s, your id is: %.2f' % (name, rating))

path = 'C:\\Users\\name\\Desktop'

print(path)
