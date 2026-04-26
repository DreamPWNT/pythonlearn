votes = ["Да", "Нет", "Да", "Да", "Воздержался",
         "Нет", "Да"]

types = []
result = []

for vote in votes:
    if vote not in types:
        types.append(vote)
        result.append((vote, 1))
    else:
        result[types.index(vote)] = (result[types.index(vote)]
                                     [0], result[types.index(vote)][1] + 1)

print(result)
