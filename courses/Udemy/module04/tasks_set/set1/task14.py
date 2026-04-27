punctuation = "!@#$%^&./,?|"
text = "Наверно на этом упражнении закончим. Хватит! Мы хотим отдыхать! #@&#@&!!!"
count = 0

while count < len(text):
    char = text[count]

    if char not in punctuation:
        print(char, end='')

    count += 1

print()
