scraped_prices = ["100,50", "5,80", "", "", "25,99", "", "17,50", "0,95", "99,00"]
normalized_price_lst = []

i, n = 0, len(scraped_prices)

while i < n:

    item = scraped_prices[i]
    if item:
        normalized_price_lst.append(float(item.replace(",", ".")))

    i += 1

print(normalized_price_lst)