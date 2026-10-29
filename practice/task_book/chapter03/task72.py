quantity = 100
start = 1

print("My number is 1")

for i in range(2, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Number is {i}. My number is Fizz-Buzz")
    elif i % 3 == 0:
        print(f"Number is {i}. My number is Buzz")
    elif i % 5 == 0:
        print(f"Number is {i}. My number is Fizz")
    else:
        print(f"Number is {i}. My number is {i}")
