scraped_prices = ["", "", "100,50", "5,80", "", "", "25,99",
                  "", "17,50", "", "0,95", "99,00", ""]

i = 0

while i < len(scraped_prices):

    item = scraped_prices[i]

    if item:
        scraped_prices[i] = float(item.replace(",", "."))

        i += 1
    else:
        scraped_prices.pop(i)

print(scraped_prices)
