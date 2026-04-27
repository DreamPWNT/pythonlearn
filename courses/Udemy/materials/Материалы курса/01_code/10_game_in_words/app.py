user_input = input("Enter something:")
vowels = "eyuioa"
vowels_count = 0
index = 0
a_count = 0

while index < len(user_input):
    char = user_input[index]
    index += 1

    if char in vowels:
        if char == "a" and a_count > 0:
            continue
        if char == "a":
            a_count += 1
        vowels_count += 1

    elif char == "t":
        break
else:
    vowels_count += 1

print(vowels_count)
