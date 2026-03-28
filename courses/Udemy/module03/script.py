result = 2*(2 - 2) / 2

print(result)

cash = 11287

bill_100 = cash // 100
bill_50 = (cash % 100) // 50
bill_20 = ((cash % 100) % 50) // 20
bill_5 = (((cash % 100) % 50) % 20) // 5
bill_1 = (((cash % 100) % 50) % 20) % 5

print(bill_100, bill_50,  bill_20, bill_5, bill_1)
