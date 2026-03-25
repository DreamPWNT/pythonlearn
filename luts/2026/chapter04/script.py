import math
import random

print(123 + 222)
print(1.5 * 4)
print(1_234_567, 0x15, bin(21))
print(2**100)
print(len(str(2**12345)))
print(math.pi)
print(math.sqrt(85))

print(random.random())
print(random.choice([1, 2, 3, 4]))

S = "Code"

print(len(S))
print(S[0])
print(S[1])
print(S[-1])
print(S[-2])
print(S)
print(S[1:3])
print(S[1:])
print(S)
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])
print(S)
print(S + "xyz")
print(S)
print(S * 8)
print(S)

S = "Z" + S[1:]

print(S)

S = "Python"
L = list(S)

print(L)

L[0] = "C"

print(L)

B = bytearray(b"app")
B.extend(b"lication")

print(B)
print(B.decode())

S = "Code"

print(S.find("od"))
print(S)
print(S.replace("od", "abl"))
print(S)

line = "aaa,bbb,cccc,dd"

print(line.split(","))

S = "Code"

print(S.upper())
print(S.isalpha())

line = "aaa,bbb,cccc,dd\n"

print(line.rstrip())
print(line.rstrip().split(","))

tool = "Python"
major = 3
minor = 3

print("Using %s version %s.%s" % (tool, major, minor + 9))
print("Using {} version {}.{}".format(tool, major, minor + 9))
print(f"Using {tool} version {major}.{minor + 9}")
print("%.2f | %+05d" % (3.14159, -62))
print("{1:,.2f} | {0}".format("sapp"[1:], 296999.256))
print(f"{296999.256:,.2f} | {'sapp'[1:]}")

print(dir(S))
print(S + "head!")
print(S.__add__("head!"))
print(help(S.replace))

print(ord("C"))
print(hex(ord("C")))
print("h\xc4\u00c4\U000000c4Ack")
