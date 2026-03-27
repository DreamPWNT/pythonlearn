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

print(ord("C"))
print(hex(ord("C")))
print("h\xc4\u00c4\U000000c4Ack")

L = [123, "text", 1.23]

print(len(L))
print(L[0])
print(L[:-1])
print(L + [4, 5, 6])
print(L * 2)
print(L)

L.append("Py")

print(L)

L.pop(2)

print(L)

M = ["bb", "aa", "cc"]
M.sort()

print(M)

M.reverse()

print(M)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(M)
print(M[1])
print(M[1][2])

col2 = [row[1] for row in M]

print(col2)

print([row[1] + 1 for row in M])
print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]]

print(diag)

doubles = [c * 2 for c in "hack"]

print(doubles)
print(list(range(4)))
print(list(range(-6, 7, 2)))
print([[x**2, x**3] for x in range(4)])
print([[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0])
print(M)

G = (sum(row) for row in M)

print(next(G))
print(next(G))
print(next(G))

print({sum(row) for row in M})
print({i: sum(M[i]) for i in range(len(M))})

D = {"name": "Pat", "job": "dev", "age": 40}

print(D["name"])

D["job"] = "mgr"

print(D)

D = {}

D["name"] = "Pat"
D["job"] = "dev"
D["age"] = 40

print(D)

pat1 = dict(name="Pat", job="dev", age=40)
pat2 = dict(zip(["name", "job", "age"], ["Pat", "dev", 40]))

print(pat1)
print(pat2)

rec = {"name": {"first": "Pat", "last": "Smith"}, "jobs": ["dev", "mgr"], "age": 40.5}

print(rec["name"])
print(rec["name"]["last"])
print(rec["jobs"])
print(rec["jobs"][-1])

rec["jobs"].append("janitor")

print(rec)

D = {"a": 1, "b": 2, "c": 3}
D["d"] = 4

print("e" in D)

if not "e" in D:
    print("missing key!")
    print("no, really")

print(D.get("a", "missing"))
print(D.get("e", "missing"))
print(D["e"] if "e" in D else 0)

D = dict(a=1, b=2, c=3)

print(D)
print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

I = iter(D.keys())

print(next(I))
print(next(I))
print(next(I))

for key in D.keys():
    print(key, "=>", D[key])

for key in D:
    print(key, "=>", D[key])

for key, value in D.items():
    print(key, "=>", value)

T = (1, 2, 3, 4)

print(len(T))
print(T + (5, 6))
print(T[0], T[1:])
print(T.index(4))
print(T.count(4))

T = (2,) + T[1:]

print(T)

T = "hack", 3.0, [11, 22, 33]

print(T)
print(T[1])
print(T[2][1])

f = open("data.txt", "w")

f.write("Hello\n")
f.write("world!\n")

f.close()

f = open("data.txt")

text = f.read()

print(text)
print(text.split())

for line in open("data.txt"):
    print(line.rstrip())

bf = open("data.bin", "wb")

bf.write(b"h\xffa\xeec\xddk\n")

bf.close()

text = open("data.bin", "rb").read()

print(text)

tf = open("unidata.txt", "w", encoding="utf-8")

tf.write("\u00c4ck")

tf.close()

print(open("unidata.txt", "r", encoding="utf-8").read())
print(open("unidata.txt", "rb").read())

X = set("hack")
Y = {"a", "p", "p"}

print(X, Y)
print(X & Y, X | Y)
print(X - Y, X > Y)
print(list(set([3, 1, 2, 1, 3, 1])))
print(set("code") - set("hack"))
print(set("code") == set("deoc"))

print(1 > 2, 1 < 2)
print(bool("hack"))

X = None

print(X)

L = [None] * 100

print(L)

L = [1, 2, 3]

print(type(L))
print(type(type(L)))
print(type(L) == type([]))
print(type(L) == list)
print(isinstance(L, list))

x: int = 1
x = "anything"
