print("Конвертер валют")
 
value = input("Из какой валюты нужно конвертировать:\n[CAD, USD, EUR]\n- ")
amount = float(input("Введите сумму, которую вы хотите конвертировать: "))
value_con = input("В какую валюту конвертируем?:\n[CAD, USD, EUR]\n- ")
 
CAD = 1  # Базовая валюта, ниже стоимость других по отношению к ней:
USD = 1.36
EUR = 1.6
 
exchange_to = value + "/" + value_con
 
if exchange_to == "CAD/USD":
    result = amount * (CAD / USD)
elif exchange_to == "USD/CAD":
    result = amount * (USD / CAD)
elif exchange_to == "CAD/EUR":
    result = amount * (CAD / EUR)
elif exchange_to == "EUR/CAD":
    result = amount * (EUR / CAD)
elif exchange_to == "USD/EUR":
    result = amount * (USD / EUR)
elif exchange_to == "EUR/USD":
    result = amount * (EUR / USD)
elif value == value_con:
    result = amount
else:
    result = 0  # на случай неправильной пары
 
print("Результат операции:")
if result == 0:
    print("Такой пары для обмена нет.")
else:
    print("Результат:", round(result, 2), value_con)


