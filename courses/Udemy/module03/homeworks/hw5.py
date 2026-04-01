phone_number = "1800-000-00-00"  # другой номер не писать сюда

if phone_number[0] != '+':
    phone_number = '+' + phone_number


print(phone_number)  # "+1800-000-00-00" должно быть так
