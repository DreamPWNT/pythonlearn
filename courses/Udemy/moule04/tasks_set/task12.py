text = input("Enter text: ")
symbol = input("Enter symbol on fragment sides: ")

print(text[text.index(symbol)+1:text.index(symbol, text.index(symbol) + 1)])

first_index = 0
second_index = len(text) - 1
text_length = len(text)
count = 0

while count < text_length:
    if text[count] == symbol:
        if first_index == 0:
            first_index = count + 1
        else:
            second_index = count

            break

    count += 1

print(text[first_index:second_index])
