score = int(input("Введите оценку: "))

if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 79 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
elif 0 <= score < 60:
    print('F')
else:
    print('Incorrect input')
