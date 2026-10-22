import math

x1 = first_x1 = input("Enter first X coordinate of point: ")
y1 = first_y1 = input("Enter first Y coordinate of point: ")
total = 0

while True:
    x2 = input("Enter next X coordinate of point: ")
    if x2 == '':
        break
    y2 = input("Enter next Y coordinate of point: ")

    total += math.sqrt((math.pow((int(x2) - int(x1)), 2)) +
                       (math.pow((int(y2) - int(y1)), 2)))

    x1 = x2
    y1 = y2

total += math.sqrt(math.pow(int(x1) - int(first_x1), 2)) + \
    (math.pow(int(y1) - int(first_y1), 2))

print(f"Perimeter = {total}")
