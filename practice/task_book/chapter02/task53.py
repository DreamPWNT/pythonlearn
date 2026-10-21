mark = float(input('Enter student mark value: '))

if mark == 4.0 or round(mark) == 4:
    print('Mark symbol is A+ or A')
elif mark == 3.7:
    print('Mark symbol is A-')
elif mark == 3.3:
    print('Mark symbol is B+')
elif mark == 3.0 or round(mark) == 3:
    print('Mark symbol is B')
elif mark == 2.7:
    print('Mark symbol is B-')
elif mark == 2.3:
    print('Mark symbol is C+')
elif mark == 2.0 or round(mark) == 2:
    print('Mark symbol is C')
elif mark == 1.7:
    print('Mark symbol is C-')
elif mark == 1.3:
    print('Mark symbol is D+')
elif mark == 1.0 or round(mark) == 1:
    print('Mark symbol is D')
elif mark == 0.0 or round(mark) == 0:
    print('Mark symbol is F')
else:
    print('Incorrect mark input!')
