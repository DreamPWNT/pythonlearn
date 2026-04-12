S1 = {43, 76, 2, 7, 8, 12, 8, 9, 3, 376}

print(S1)

S1.add(45678)

S2 = {342, 34, 67, 7, 1, 1, 7, 8, 23, 54, 8, 32,
      3, 78, 2, 6, 32, 21, 8, 732, 78, 98, 4, 43}

print(S2)

S3 = S1 & S2

print(list(S3))
print(list(S1 | S2))
print(list(S1 & S2))
print(list(S1 ^ S2))
print(list(S1 - S2))
