ip_info = {
    "ip": "8.8.8.8",
    "version": "IPv4",
    "city": "Mountain View",
    "region": "California",
    "region_code": "CA",
    "country": "US",
    "country_name": "United States",
    "country_code": "US",
    "country_capital": "Washington",
    "postal": "94043"
}


slugs = {"Все товары": "all", "Кухня": "kuhnya", "Спальня": "spalnya"}


# slug - фрагмент пути в url адресе от домена
# https://www.furniture.com/kuhnya

categories = [
    {"pk": 6, "name": "Все товары", "slug": "all"},
    {"pk": 7, "name": "Кухня", "slug": "kuhnya"},
    {"pk": 8, "name": "Спальня", "slug": "spalnya"},
    {"pk": 9, "name": "Гостинная", "slug": "gostinnaya"},
    {"pk": 10, "name": "Офис", "slug": "ofis"},
    {"pk": 11, "name": "Декор", "slug": "dekor"},
]


temps_celsius = {
    "06:00": -1.5,
    "07:00": -0.8,
    "08:00": 2.8,
    "09:00": 5.6,
    "10:00": 8.4,
    "11:00": 11.2,
    "12:00": 14.7,
    "13:00": 17.0,
    "14:00": 18.3,
    "15:00": 19.1,
    "16:00": 19.4,
    "17:00": 18.8,
    "18:00": 17.0,
    "19:00": 14.5,
    "20:00": 11.2,
    "21:00": 7.5,
    "22:00": 4.0
}


views = [
    ("Ann", 1), ("Bob", 1), ("Kate", 1),
    ("Ann", 1), ("Bob", 2), ("Mike", 2),
    ("Kate", 2), ("Bob", 2), ("John", 3),
    ("Ann", 3), ("Kate", 3), ("Ann", 3),
    ("Ann", 3),
]


post_1_viewers = ["Ann", "Bob", "Kate", "Ann"]
post_2_viewers = ["Bob", "Mike", "Kate", "Bob"]
post_3_viewers = ["John", "Ann", "Kate", "Ann", "Ann"]


warehouse_A = {
    "laptop": 12,
    "mouse": 50,
    "keyboard": 30,
    "monitor": 10,
}

warehouse_B = {
    "mouse": 40,
    "keyboard": 10,
    "tablet": 5,
    "printer": 2,
}
