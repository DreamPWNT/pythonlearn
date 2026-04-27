def get_data():
    data = (["44519", 0.91], ["96424", 0.9], ["345543", 0.9],
              ["44246", 0.92], ["64687", 0.91], ["86776", 0.91])
    return data

def get_exchange_rate():
    return 0.89

def get_percent_of(value, part):
    if value <= 0 or part < 0:
        return False

    return round(part / value * 100, 2)

def get_processed_data():
    percent_list = []
    exchangers = get_data()
    exchange_rate = get_exchange_rate()
    for exchanger in exchangers:
        percent = get_percent_of(exchange_rate, exchanger[1])
        if percent:
            percent_list.append(percent)
            exchanger.append(percent)

    return percent_list, exchangers


x, y = get_processed_data()
print(x)
