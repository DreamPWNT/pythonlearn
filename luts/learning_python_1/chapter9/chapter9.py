from collections import namedtuple
import pickle
import json
import struct

file_path = "luts/learning_python_1/data/"
# file_path = ""

T = tuple("spam")

print(T)
print((1, 2) + (3, 4))
print((1, 2) * 4)

T = (1, 2, 3, 4)

print(T[0], T[1:3])

T = ("cc", "aa", "dd", "bb")

tmp = list(T)
tmp.sort()

print(tmp)

T = tuple(tmp)

print(T)

T = ("cc", "aa", "dd", "bb")

print(sorted(T))

T = (1, 2, 3, 4, 5)
L = [x + 20 for x in T]

print(L)

T = (1, 2, 3, 2, 4, 2)

print(T.index(2))
print(T.index(2, 2))
print(T.count(1))

T = (1, [2, 3], 4)
T[1].append(5)

print(T)

bob = ("Bob", 40.5, ["dev", "mgr"])

print(bob)
print((bob[0], bob[2]))

bob = dict(name="Bob", age=40.5, jobs=["dev", "mgr"])

print(bob)
print((bob["name"], bob["jobs"]))
print(tuple(bob.values()))
print(list(bob.items()))

Rec = namedtuple("Rec", ["name", "age", "jobs"])
bob = Rec("Bob", age=40.5, jobs=["dev", "mgr"])

print(bob)
print(bob[0])
print(bob[2])
print(bob.name)
print(bob.jobs)

O = bob._asdict()

print(O["name"], O["jobs"])
print(O)

bob = Rec("Bob", age=40.5, jobs=["dev", "mgr"])
name, age, jobs = bob

print(name, jobs)

for x in bob:
    print(x)

myfile = open(file_path + "myfile.txt", "w")

myfile.write("hello text\n")
myfile.write("goodbye text file\n")

myfile.close

myfile = open(file_path + "myfile.txt")

print(repr(myfile.readline()))
print(repr(myfile.readline()))
print(repr(myfile.readline()))

myfile = open(file_path + "myfile.txt").read()

print(repr(myfile))
print(myfile)

for line in open(file_path + "myfile.txt"):
    print(line, end="")

data = open(file_path + "data.bin", "w")

data.write("spam\n")
data.close()

data = open(file_path + "data.bin", "rb").read()

print(repr(data), data[4:8])

X, Y, Z = 43, 44, 45
S = "Spam"
D = {"a": 1, "b": 2}
L = [1, 2, 3]

F = open(file_path + "datafile.txt", "w")

F.write(S + "\n")
F.write("{},{},{}\n".format(X, Y, Z))
F.write(str(L) + "$" + str(D) + "\n")

F.close()

chars = open(file_path + "datafile.txt").read()

print(repr(chars))
print(chars)

F = open(file_path + "datafile.txt")

line = F.readline()

print(repr(line.rstrip()))
print(repr(line))

line = F.readline()

print(repr(line))

parts = list(map(int, line.split(",")))

print(parts)

line = F.readline()

print(repr(line))

parts = line.split("$")

print(repr(parts))

print(eval(parts[0]))
print(eval(parts[1]))

objects = [eval(part) for part in parts]

print(objects)

D = {"a": 1, "b": 2}

F = open(file_path + "datafile.pkl", "wb")

pickle.dump(D, F)

F.close()

F = open(file_path + "datafile.pkl", "rb")

E = pickle.load(F)

print(repr(E))
print(open(file_path + "datafile.pkl", "rb").read())

name = dict(first="Bob", last="Smith")
rec = dict(name=name, job=["dev", "mgr"], age=40.5)

print(name, rec)

S = json.dumps(rec)

print(repr(S))

O = json.loads(S)

print(repr(O))
print(O == rec)

json.dump(rec, fp=open(file_path + "testjson.txt", "w"), indent=4)

print(open(file_path + "testjson.txt").read())

P = json.load(open(file_path + "testjson.txt"))

print(P)

F = open(file_path + "struct.bin", "wb")

data = struct.pack(">i4sh", 7, b"spam", 8)

print(data)

F.write(data)

F.close()

F = open(file_path + "struct.bin", "rb")

data = F.read()

print(data)

values = struct.unpack(">i4sh", data)

print(values)

L = ["abc", [(1, 2), ([3], 4)], 5]

print(L[1], "|", L[1][1], "|", L[1][1][0], "|", L[1][1][0][0])

X = [1, 2, 3]
L = ["a", X, "b"]
D = {"x": X, "y": 2}

X[1] = "surprise"

print(X, L, D)

L = [1, 2, 3]
D = {"a": 1, "b": 2}

A = L[:]
B = D.copy()

A[1] = "Ni"
B["c"] = "spam"

print(A, B, L, D)

L1 = [1, {"a": 3}]
L2 = [1, {"a": 3}]

print(L1 == L2, L1 is L2)

S1 = "spam"
S2 = "spam"

print(S1 == S2, S1 is S2)

S1 = "a longer string gjfdklojiowerjgiowejgrwiogjweioggfdsknhjl;dsfg,m.jhgjsfklde;imuop432g5mpiou345b6mopuib34567imojpub34567ijmopw45bey6mjkolhwretsbjtyo5wrelu60io345mu6bjyiot5r4mnubyj456oiemniju7op45ey6r"
S2 = "a longer string gjfdklojiowerjgiowejgrwiogjweioggfdsknhjl;dsfg,m.jhgjsfklde;imuop432g5mpiou345b6mopuib34567imojpub34567ijmopw45bey6mjkolhwretsbjtyo5wrelu60io345mu6bjyiot5r4mnubyj456oiemniju7op45ey6r"

print(S1 == S2, S1 is S2)

L1 = [1, ("a", 3)]
L2 = [1, ("a", 2)]

print(L1 < L2, L1 == L2, L1 > L2)

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print(L, X, Y)

L[1] = 0

print(X, Y)

D = {
    "personal": {
        "name": "Dmitriy",
        "second_name": "Viktorovich",
        "last_name": "Dolganov",
    },
    "age": 37,
    "work": {
        "post": "Senior PHP developer",
        "work_place": "MIIT",
    },
    "contact_info": {
        "adress": "Bobrovo, Lesnaya street 24-1-241",
        "phone": "+380633844468",
        "e-mail": "dreampwnt@gmail.com",
    },
}

print(D, D["personal"]["last_name"], D["work"]["post"], D["contact_info"]["phone"])

f = open("hw.txt", "w")

f.write("Hello file world!\n")

f.close()


f = open("hw.txt")

print(repr(f.read()))
