import sys

print("one" "two")

s = "a\nb\tc"

print(s)
print(r"c:\new\file1.txt")
print("c:\\new\\file1.txt")

mantra = """Python is a 
            best languiage
            in the world"""

print(mantra)
print(len("abc"))
print("abc" + "def")
print("Ni!" * 6)

myjob = "hacker"

for c in myjob:
    print(c, end="|")

print("k" in myjob)
print("z" in myjob)
print("spam" in "abcdefspamkloijhy")

S = "spam"

print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = "abcdefghijklmnopqrstuvwxyz"

print(S[1:22:4])
print(S[::3])
print(S[::-1])

print("spam"[1:3])
print("spam"[slice(1, 3)])
print("spam"[::-1])
print("spam"[slice(None, None, -1)])
print(str("spam"), repr("spam"))

S = "42"

print(int(S) + 128)
print(S + str(33))
print(ord("Z"))
print(chr(33))
print(chr(10))

for c in "abcdefghijklmnopqrstuvwxyz":
    print(f"Symbol {c} match ASCII code:", ord(c))

print("Factorio is a %s %s in the world" % ("best", "game"))
print("Factorio is a %d %s in the world" % (4, "fun"))

S = "sjsjdfghalgbkm"

print(S.replace("gh", "zz"))
print(S.find("zz"))
print(S.find("bkm"))
print("bkm" in S)

S2 = "God bless America"

print(S2.split())

S3 = "This lans was made for you and me\n"

print(S3)

S3 = S3.rstrip()

print(S3.upper())
print(S3.isalpha())
print(S3.endswith("America"))
print(S3.endswith("you"))
print(S3.endswith("me"))
print(S3.startswith("land"))
print(S3.startswith("USA"))
print(S3.startswith("This"))

print("that is %d %s bird!" % (1, "dead"))

exclamation = "Ni"

print("The knight who say %s!" % exclamation)
print("%d %s %g you" % (1, "spam", 4.0))
print("%s -- %s -- %s" % (42, 3.1415926, [1, 2, 3]))

x = 1234

print("integers: ...%d...%-6d...%06d" % (x, x, x))

x = 1.23456789

print("%e | %f | %g" % (x, x, x))
print("%-6.2f | %05.2f | %+06.1f" % (x, x, x))
print("%s" % x, str(x))
print("%f, %.2f, %.*f" % (1 / 3.0, 1 / 3.0, 10, 1 / 3.0))

D = {"qty": 1, "food": "spam"}
print("%(qty)d more %(food)s" % D)

values = {"db_name": "dt", "encoding": "utf"}
reply = """I want to use 
database %(db_name)s 
in %(encoding)s encoding
"""

print(reply % values)
print(vars())
print(
    "My job is %(myjob)s, a thik that %(S2)s and my favorite db is: %(values)s" % vars()
)

template = "{0}, {1} and {2}"

print(template.format("spam", "ham", "eggs"))

template = "{motto}, {pork} and {food}"

print(template.format(motto="spam", pork="ham", food="eggs"))

template = "{motto}, {0} and {food}"

print(template.format("ham", motto="spam", food="eggs"))

template = "{}, {} and {}"

print(template.format("spam", "ham", "eggs"))

print("My mega {1[kind]} runs on {0.platform}".format(sys, {"kind": "computer"}))

somelist = list("SPAM")

print("first={0[0]}, third={0[2]}".format(somelist))
print("first={0}, last={1}".format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]

print("first={0}, last={1}, middle={2}".format(*parts))
print("{0:10} = {1:10}".format("spam", 123.4567))
print("{0:>10} = {1:<10}".format("spam", 123.4567))
print("{0.platform:>10} = {1[kind]:<10}".format(sys, dict(kind="laptop")))
print("{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159))
print("{0:f}, {1:.2f}, {2:06.2f}".format(3.14159, 3.14159, 3.14159))
print("{0:X}, {1:o}, {2:b}".format(255, 255, 255))

a, b, c = input().split()
print(a.ljust(3, "0") + "\n" + b.ljust(3, "0") + "\n" + c.ljust(c, "0"))
