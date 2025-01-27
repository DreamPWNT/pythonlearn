line = "Hello, my name is [u-1061][u-1072][u-1082][u-1080]!"
counter = 0

decrypted_line = ""
flag = True

for ch in line:
    if ch == "[":
        flag = False
        print(line[counter + 3 : counter + 7])
        decrypted_line += chr(int(line[counter + 3 : counter + 7]))
        print(decrypted_line)
    elif ch == "]":
        flag = True
    elif ch != "[" and ch != "]" and flag == True:
        decrypted_line += ch

    counter += 1

print(decrypted_line)

print(max("9", "10", "11"))

S = "Толстой А.Н., «Петр Первый»"

first_space = S.find(" ")
second_space = S.find(" ", first_space + 1)
last_name = S[0:first_space]
book_name = S[second_space + 1 :]
print(first_space, second_space, last_name, book_name)
