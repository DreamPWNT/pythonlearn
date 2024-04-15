def times(x, y):
    return x * y


x = times(2, 3)

print(x)
print(times("Ni", 7))


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


s1 = "SPAM"
s2 = "SCAM"

print(intersect(s1, s2))
print(intersect([1, 2, 3], (1, 4)))
