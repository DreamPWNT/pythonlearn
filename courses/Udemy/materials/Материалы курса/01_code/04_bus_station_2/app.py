num_tickets = 40  # количество проданных билетов (пассажиров)
bus_capacity = 20  # количество мест в автобусе

bus_quantity = num_tickets // bus_capacity  # Кол-во полных автобусов
num_tickets_left = num_tickets % bus_capacity  # Кол-во оставшихся пассажиров

has_partial_bus = False
empty_seats = 0

if num_tickets_left:
    if num_tickets_left >= bus_capacity / 2:
        bus_quantity += 1
        has_partial_bus = True

        empty_seats = bus_capacity - num_tickets_left
        num_tickets_left = 0


print(bus_quantity, num_tickets_left, has_partial_bus, empty_seats)

# Нужно получить такие данные:
# Количество автобусов: полных и + 1 если 1 заполнен на половину и более
# Количество оставшихся неразмещенных пассажиров
# True если 1 автобус не полный, иначе False
# Кол-во пустых мест, если 1 автобус не полный
