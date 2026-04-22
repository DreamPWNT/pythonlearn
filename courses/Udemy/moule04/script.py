count = 0

while count < 5:
    print(count)

    count += 1

print(count)

password = input('Create your password:\n')

while True:
    if len(password) < 8:
        print('Password must be at least 8 characters long')

        password = input('Enter your password again:\n')
    else:
        break

print(password)

user_input = input('Enter something:\n')

vowels = 'eyuioa'
vowels_count = 0
index = 0
a_count = 0

while index < len(user_input):
    char = user_input[index]
    index += 1

    if char == 'a' and a_count > 0:
        continue

    if char in vowels:
        if char == 'a' and a_count > 0:
            continue
        if char == 'a':
            a_count += 1

        vowels_count += 1
    elif char == 't':
        break
else:
    vowels_count += 1

print(vowels_count)
