# Список собранных с сайта цен.
scraped_prices = ["100,50", "5,80", "", "",
                  "25,99", "", "17,50", "0,95", "99,00"]

# Нужно в этот список поместить цены преобразованные в тип float,
# пустые строки не добавлять.
normalized_price_lst = []

count = 0

while count < len(scraped_prices):
    if scraped_prices[count]:
        normalized_price_lst.append(
            float(scraped_prices[count].replace(',', '.')))

    count += 1


print(normalized_price_lst)
