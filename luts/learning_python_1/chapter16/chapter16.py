def times(x, y):
    return x * y


print(times(2, 4))

x = times(3, 7)

print(x)
print(times("Ni!", 8))


def intersect(seq1, seq2):
    res = []

    for x in seq1:
        if x in seq2:
            res.append(x)

    return res


s1 = "SPAM"
s2 = "SCAM"

print(intersect(s1, s2))
print([x for x in s1 if x in s2])
print(intersect([1, 2, 3], (1, 4)))
