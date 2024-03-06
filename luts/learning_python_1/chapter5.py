import math

print(int(3.1415))
print(float(333))

a = 3
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 + b)
print(b / 2 + a)
print(b / (2.0 + a))

num = 1 / 3.0
print(num)
print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))

print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 6

print(X < Y < Z)
print(X < Y and Y < Z)
print(X > Y < Z)
print(X < Y and X > Z)
print(1 < 2 < 44 < 1 < 0 < 5)
print(1.1 + 2.2 == 3.3)

print(3.0 // 2.0)
print(3.0 // 2)
print(3 // 2)
print(3 // -2)

print(0o1, 0o20, 0o377)
print(0x01, 0x10, 0xFF)
print(0b1, 0b10000, 0b11111111)

print(0xFF, (15 * (16 ** 1) + 15 * (16 ** 0)))
print(0x25, (2 * (16 ** 1) + (5 * (16 ** 0))))
print(0o57160, (5 * (8 ** 4)) + (7 * (8 ** 3)) + (1 * (8 ** 2)) + (6 * (8 ** 1)) + (0 * (8 ** 0)))
print(0b100010101, (1 * (2 ** 8)) + (0 * (2 ** 7)) + (0 * (2 ** 6)) + (0 * (2 ** 5)) + (1 * (2 ** 4)) + (0 * (2 ** 3)) + (1 * (2 ** 2)) + (0 * (2 ** 1)) + (1 * (2 ** 0)))
print(oct(27389576289), hex(27389576289), bin(27389576289))

print(1 << 2)
print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))