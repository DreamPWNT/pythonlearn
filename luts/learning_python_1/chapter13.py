from os import listdir

x = "spam"

while x:
    print(x, end=" ")
    x = x[1:]

a = 0
b = 10

while a < b:
    print(a)
    a += 1

Y = ...

print(Y)

x = 10

while x:
    x = x - 1

    if x % 2 != 0:
        continue

    print(x, end=" ")

while True:
    name = input("Enter name: ")

    if name == "stop":
        break

    age = input("Enter age: ")

    print("Hello " + name + " => " + age)

for x in "spam":
    if x == "p":
        break

print(x)

for x in ["spam", "eggs", "ham"]:
    print(x, end=" ")

lst = [1, 2, 3, 4]
sum = 0
prod = 1

for x in lst:
    sum += x

for x in lst:
    prod *= x

print(sum)
print(prod)

S = "lumberjack"

for ch in S:
    print(ch, end=" ")

T = ("and", "I'm", "okay")

for s in T:
    print(s, end=" ")

T = [(1, 2), (3, 4), (5, 6)]

for a, b in T:
    print(a, b)

D = {"a": 1, "b": 2, "c": 3}

for key in D:
    print(key, "=>", D[key])

print(list(D.items()))

for key, value in D.items():
    print(key, "=>", value)

for a, b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)

for a, *b, c in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

items = ["s", (1, 2, 3), 12, 1533.97, {"a": 1, "b": 5}, [55, 66, 88]]
tests = ["a", ["bbb", "ddd"], 9999.9999, 12, {"a": 1, "b": 5}, (321, 123), "s", 1533.97]

for test in tests:
    for item in items:
        if item == test:
            print(item, "was found =))))))")
            break
    else:
        print(test, "not found (((((")

for test in tests:
    if test in items:
        print(test, "was found =))))))")
    else:
        print(test, "not found (((((")

L2 = []

for test in tests:
    if test in items:
        L2.append(test)

print(L2)

L3 = []
S2 = "spafjnkjldfgj;lahhgj"
S3 = "vbnpqqwjugtiuohidhnkfjdsl"

for ch1 in S2:
    for ch2 in S3:
        if ch2 == ch1:
            L3.append(ch2)
            break

print(L3)
print(listdir())

file = open("pythonlearn/luts/learning_python_1/hwfile.txt")

while True:
    char = file.read(1)

    if not char:
        break

    print(char)

for char in open("pythonlearn/luts/learning_python_1/hwfile.txt"):
    print(char)

file2 = open("pythonlearn/luts/learning_python_1/log.txt")

while True:
    line = file2.readline()

    if not line:
        break

    print(line.rstrip())
