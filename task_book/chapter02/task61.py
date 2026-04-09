auto_reg_num = input('Enter auto registration number: ')

if len(auto_reg_num) == 6 and auto_reg_num[0:3].isupper() and auto_reg_num[3:].isdigit():
    print('Old number format')
elif len(auto_reg_num) == 7 and auto_reg_num[0:4].isdigit() and auto_reg_num[4:].isupper():
    print('New number format')
else:
    print('Unknown format!')
