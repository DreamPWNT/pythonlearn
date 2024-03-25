x = "killer rabbit"

if x == "roger":
    print("shave and a haircut")
elif x == "bugs":
    print("what's up doc?")
else:
    print("Run away! Run away!")

choice = "ham"

print({"spam": 1.25, "ham": 1.99, "eggs": 0.99, "bacon": 1.10}[choice])

if choice == "spam":
    print(1.25)
elif choice == "ham":
    print(1.99)
elif choice == "eggs":
    print(0.99)
elif choice == "bacon":
    print(1.10)
else:
    print("Bad choice")

branch = {"spam": 1.25, "ham": 1.99, "eggs": 0.99}

print(branch.get("spam", "Bad choice"))
print(branch.get("bacon", "Bad choice"))

choice = "bacon"

if choice in branch:
    print(branch[choice])
else:
    print("Bad choice")

try:
    print(branch[choice])
except KeyError:
    print("Bad choice")

x = "SPAM"

if "rubbery" in "shrubbery":

    print(x * 8)

    x += "NI"
    if x.endswith("NI"):

        x *= 2

        print(x)
A = "t" if "spam" else "f"

print(A)

L = [1, 0, 2, 0, "spam", "", "ham", []]

print(list(filter(bool, L)))
print([x for x in L if x])
print(any(L), all(L))
