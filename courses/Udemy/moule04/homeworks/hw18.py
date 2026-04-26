country_codes = ["754", "690", "450"]  # Канада, Китай, Япония

products = ["4506436054267", "7547682958186", "6900626469201",
            "7543817559796", "7544194259711", "6900590565047",
            "6901237511586", "4502714135954", "4500295752923",
            "6901237511587"]


for country_code in country_codes:
    print(f'{country_code}: ', end='')

    for product in products:
        if product.startswith(country_code):
            print(f'{product} ', end='')

    print()
