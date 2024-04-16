import sys

nudge = 1
wink = 2
A, B = nudge, wink

print(A, B)

[C, D] = [nudge, wink]

print(C, D)

[a, b, c] = (1, 2, 3)

print(a, b, c)

(a, b, c) = "ABC"

print(a, c)

L = [1, 2, 3, 4]

while L:
    front, L = L[0], L[1:]

    print(front, L)

seq = [1, 2, 3, 4]
a, *b = seq

print(a, b)

*a, b = seq

print(a, b)

x = "spam"
y = 99
z = ["eggs"]

print(x, y, z, sep="...", file=open("luts/learning_python_1/printfile.txt", "w"))

temp = sys.stdout
sys.stdout = open("luts/learning_python_1/log.txt", "a")

print("spam")
print(1, 2, 3)

sys.stdout.close()
sys.stdout = temp

print("back here")
print(open("luts/learning_python_1/log.txt", "r").read())

sys.stderr.write(("Bad" * 8) + "\n")
print("Bad" * 8, file=sys.stderr)
