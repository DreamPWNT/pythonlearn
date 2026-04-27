from time import strftime
# Стандарт времени универсальный ISO 8601 выглядит так: strftime("%Y-%m-%dT%H:%M:%S")
# Формат текущей локали системы (без унив. ISO стандарта) strftime("%c") это как asctime()
locale = "en-US"

def pretty_time(
    *, date_delimiter=".", time_delimiter=":" , time_first=False, us_format=False
):
    if us_format:
        date_format = f"%m{date_delimiter}%d{date_delimiter}%Y"
        time_format = f"%I{time_delimiter}%M{time_delimiter}%S %p"
    else:
        date_format = f"%d{date_delimiter}%m{date_delimiter}%Y"
        time_format = f"%H{time_delimiter}%M{time_delimiter}%S"

    # if time_first:
    #     pattern = f"{time_format} {date_format}"
    # else:
    #     pattern = f"{date_format} {time_format}"

    pattern = f"{time_format} {date_format}" if time_first else f"{date_format} {time_format}"
    return strftime(pattern)


time_now = pretty_time(
    date_delimiter="/" if locale == "en-US" else ".",
    time_delimiter="-",
    us_format=locale == "en-US",
    )
print(time_now)

    
