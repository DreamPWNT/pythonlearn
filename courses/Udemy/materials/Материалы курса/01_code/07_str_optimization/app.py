ascii = 'a' * 10
not_only_ascii = 'a' * 9 + '😃😃'

print(ascii.__sizeof__() - ''.__sizeof__())
print(not_only_ascii.__sizeof__() - '😃'.__sizeof__())


