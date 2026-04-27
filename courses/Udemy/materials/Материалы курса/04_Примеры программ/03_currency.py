print('Конвертер валют')

# курс обмена (примерные значения)
usd_to_pln = 4.0   # 1 доллар = 4.0 злотых
eur_to_pln = 4.3   # 1 евро = 4.3 злотых

amount = float(input("Введите сумму: "))
currency = input('Введите валюту ("usd" или "eur"): ')

if currency == "usd":
    result = amount * usd_to_pln
    print(str(amount) + " USD = "+ str(result) + " PLN")
elif currency == "eur":
    result = amount * eur_to_pln
    print(str(amount) + " EUR = "+ str(result) + " PLN")
else:
    print("Ошибка: неизвестная валюта")


