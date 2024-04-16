import pickle
import json
import struct

print((1, 2) + (3, 4))
print((1, 2) * 4)

T = (1, 2, 3, 4)

print(T[0], T[1:3])

T = ("cc", "aa", "dd", "bb")

tmp = list(T)
tmp.sort()

T = tuple(tmp)

print(T)

T = ("cc", "aa", "dd", "bb")

print(sorted(T))

print([x for x in range(1, 30)])

myfile = open("luts/learning_python_1/data/myfile.txt", "w")

print(myfile.write("hello text file\n"))
print(myfile.write("goodbye text file\n"))

myfile.close()

myfile = open("luts/learning_python_1/data/myfile.txt")

print(myfile.readline(), end="")
print(myfile.readline(), end="")
print(myfile.readline(), end="")
print(open("luts/learning_python_1/data/myfile.txt").read())

for line in open("luts/learning_python_1/data/myfile.txt"):
    print(line, end="")

X, Y, Z = 43, 44, 45
S = "Spam"
D = {"a": 1, "b": 2}
L = [1, 2, 3]

F = open("luts/learning_python_1/data/datafile.txt", "w")
F.write(S + "\n")
F.write("%s,%s,%s\n" % (X, Y, Z))
F.write(str(L) + "$" + str(D) + "\n")
F.close()

chars = open("luts/learning_python_1/data/datafile.txt").read()

print(chars)

F = open("luts/learning_python_1/data/datafile.txt")

line = F.readline()
line.rstrip()

print(line)

line = F.readline()
line.rstrip()

numbers = [int(x) for x in line.split(",")]

print(numbers)

line = F.readline()
line.rstrip()
L = eval(line.split("$")[0])
D = eval(line.split("$")[1])

print(L)
print(D)

D1 = {"a": 1, "b": 2}
D2 = [3, 4, 5, 6, 76, 78, 89]
data = {"d1": D1, "d2": D2}

F = open("luts/learning_python_1/data/datafile.pkl", "wb")

pickle.dump(data, F)
F.close()

F = open("luts/learning_python_1/data/datafile.pkl", "rb")
E = pickle.load(F)
print(E)

name = dict(first="Bob", last="Smith")
rec = dict(name=name, job=["dev", "mgr"], age=40.5)

S = json.dumps(rec)

print(S)

O = json.loads(S)

print(O)

print(O == rec)

json.dump(rec, fp=open("luts/learning_python_1/data/testjson.json", "w"), indent=2)
print(open("luts/learning_python_1/data/testjson.json").read())

P = json.load(open("luts/learning_python_1/data/testjson.json"))

print(P)

F = open("luts/learning_python_1/data/data.bin", "wb")
data = struct.pack(">i4sh", 7, b"spam", 8)

print(data)

F.write(data)
F.close()

F = open("luts/learning_python_1/data/data.bin", "rb")

data = F.read()

print(data)

values = struct.unpack(">i4sh", data)

print(values)

L = ["abc", [(1, 2), ([3], 4), 5]]

print(L[1])
print(L[1][1])
print(L[1][1][0])
print(L[1][1][0][0])

X = [1, 2, 3]
L = ["a", X, "b"]
D = {"x": X, "y": 2}

print(X)

X[1] = "surprise"

print(X)
print(L)
print(D)

L = [1, 2, 3]
D = {"a": 1, "b": 2}
A = L[:]
B = D.copy()
A[1] = "Ni!"
B["c"] = "spam"

print(L, D)
print(A, B)

L1 = [1, {"a": 3}]
L2 = [1, {"a": 3}]

print(L1 == L2, L1 is L2)

S1 = "spam"
S2 = "spam"

print(S1 == S2, S1 is S2)

L1 = [1, ("a", 3)]
L2 = [1, ("a", 2)]

print(L1 > L2, L1 == L2, L1 < L2)

K = (1, 2, 3, 4, 5)

print(len(K))

K1 = (4, 5, 6)
K2 = (1,) + K1[1:3]

print(K2)

print(2**16)
print(2 / 5, 2 / 5.0)
print("spam" + "eggs")

S = "ham"

print("eggs" + S)
print(S * 5)
print(S[:0])
print("green %s and %s" % ("eggs", S))
print("green {0} and {1}".format("eggs", S))
print(("x",)[0])
print(("x", "y")[1])

L = [1, 2, 3] + [4, 5, 6]

print(L, L[:], L[:0], L[:-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])

L.reverse()

print(L)

L.sort()

print(L)
print(L.index(4))
print({"a": 1, "b": 2}["b"])

D = {"x": 1, "y": 2, "z": 3}
D["w"] = 0

print(D)
print(D["x"] + D["w"])

D[(1, 2, 3)] = 4

print(D)
print(list(D.keys()))
print(list(D.values()))
print([[]], ["", [], (), {}, None])

L = [0, 1, 2, 3]

# print(L[4])
print(L[-1000:100])

L[3:1] = ["?"]

print(L)

L = [4, 5, 6, 7]
L[2] = []

print(L)

L[2:3] = []

print(L)

# del L[0]
# del([1:])
# L[1:2] = 1
print(L)

X = "spam"
Y = "eggs"
X, Y = Y, X
print(X, Y)

D = {}
D[1] = "a"
D[2] = "b"
D[(1, 2, 3)] = "c"

print(D)

D = {"a": 1, "b": 2, "c": 3}
D["d"] = "spam"

print(D)

S1 = "spam"
D1 = [1, 2, 3]

# print(D + D1)

D1.append(4)
# S1.append("sss")

print(D1)
# print(D1.keys())

S = "spam"

print(S[0][0][0][0][0])


D2 = ["s", "p", "a", "m"]

print(D2[0][0][0][0][0])

S2 = "spam"
print(S[0] + "l" + S[2:])

Dream = {
    "name": "Dmitriy",
    "second_name": "Viktorovich",
    "lastname": "Dolganov",
    "age": 36,
    "adress": "Sevastopolskiy 38-53",
    "e_mail": "dimon_33@mail.ru",
    "phone": "+380633844468",
}

print(Dream)

newfile = open("luts/learning_python_1/data/hwfile.txt", "w")
newfile.write("Hello file world!\n")
newfile.close()

newfile = open("luts/learning_python_1/data/hwfile.txt", "r")

for line in newfile:
    print(line, end="")

newfile = open("luts/learning_python_1/data/hwfile.txt", "r")

print(newfile.readline(), end="")
