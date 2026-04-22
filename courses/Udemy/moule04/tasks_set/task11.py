word = "иладеп"
right_word = ''
count = len(word) - 1

print(word[::-1])

while count >= 0:
    right_word += word[count]

    count -= 1

print(right_word)

count = len(word) - 1

while count >= 0:
    print(word[count], end='')

    count -= 1
