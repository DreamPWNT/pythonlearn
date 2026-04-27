exchangers = (["44519", 0.91], ["96424", 0.9], ["345543", 0.9], ["44246", 0.92], ["64687", 0.91], ["86776", 0.91])
exchange_rate = 0.89

def percent_of(value, part, /, *, numeric=True):
    if value <= 0 or part < 0:
        return False

    percent = part / value * 100
    if numeric:
        return round(percent, 2)
    return str(round(percent, 2)) + " %"


percent_list = []
for exchanger in exchangers:
    percent = percent_of(exchange_rate, exchanger[1], numeric=False)
    percent_list.append(percent)
    exchanger.append(percent)

print(percent_list)
print(exchangers)
