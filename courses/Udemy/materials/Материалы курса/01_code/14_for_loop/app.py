# widgets = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#"]

scraped_prices = ["", "", "100,50", "5,80", "", "", "25,99",
                  "", "17,50", "", "J0,95", "99,00", ""]

new = []

for item in scraped_prices:

    if not item:
        continue
    
    if not item.replace(",", "").isdigit():
        new.clear()
        without_price = None
        break
    
    item = float(item.replace(",", "."))
    new.append(item)
else:
    without_price = len(scraped_prices) - len(new)

print(new)
print(without_price)