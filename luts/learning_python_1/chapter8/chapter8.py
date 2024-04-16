print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(["Ni!"] * 4)
print(str([1, 2]) + "34")

res = [c * 4 for c in "SPAM"]

print(res)

L = ["spam", "Spam", "SPAM!"]

print(L[2])
print(L[-2])
print(L[1:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[2][2])

L[0:2] = ["eat", "more"]

print(L)

D = {}

print(D)

D = {"name": "Bob", "age": 40}

print(D)

E = {"cto": {"name": "Bob", "age": 40}}

print(E)

D = dict(name="Bob", age=40)

print(D)

D = dict([("name", "Bob"), ("age", 40)])

print(D)
print(D.keys())
print(D.values())
print(D.items())
print(list(D.keys()))
print({x: x * 2 for x in range(10)})

D = {"spam": 2, "ham": 1, "eggs": 3}

print(D)
print(D["spam"])
print(len(D))
print("ham" in D)
print(list(D.keys()))

D["ham"] = ["grill", "bake", "fry"]

print(D)

del D["eggs"]

print(D)

D["brunch"] = "Bacon"

print(D)

print(D.get("spam"))
print(D.get("toast"))
print(D.get("toast", "jam"))

D2 = {"spam": 333, "vodka": 1.0, "seledka": 75}
D.update(D2)

print(D)
print(D.pop("seledka"))
print(D)

table = {"1975": "Holy Grail", "1979": "Life of Brian", "1983": "The meaning of life"}
year = "1983"
movie = table[year]

print(movie)

for year in table:
    print(year + "\t" + table[year])

print(table.items())

table[1.65678] = "aasaa"
print(table)
