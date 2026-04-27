card = ["1111", "2222", "3333", "4444"]

card_number = ''

for part in card:
    card_number += f'{part}-'

card_number = card_number[:-1]

print(card_number)
