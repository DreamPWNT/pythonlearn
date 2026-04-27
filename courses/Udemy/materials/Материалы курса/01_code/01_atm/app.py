cash  = 287
# 100 50 20 5 1

hundred = cash // 100
rest_of = cash % 100

fifty = rest_of // 50
rest_of = rest_of % 50

twenty = rest_of // 20
rest_of = rest_of % 20

five = rest_of // 5
rest_of = rest_of % 5

one = rest_of

print(hundred, fifty, twenty, five, one)
