words = ["Python", "это", "круто"]

result = ""

for word in words:
    result += f'{word}, '

result = result[:-2]

print(result)
