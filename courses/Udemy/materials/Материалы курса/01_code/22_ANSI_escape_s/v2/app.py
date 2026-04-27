__fg = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37"
}

__bg = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47"
}

__fgbright = {
    "black": "90",
    "red": "91",
    "green": "92",
    "yellow": "93",
    "blue": "94",
    "magenta": "95",
    "cyan": "96",
    "white": "97"
}

__bgbright = {
    "black": "100",
    "red": "101",
    "green": "102",
    "yellow": "103",
    "blue": "104",
    "magenta": "105",
    "cyan": "106",
    "white": "107"
}

__effects = {
    "reset": "0",           # Сброс всех эффектов
    "bold": "1",            # Жирный текст
    "underline": "4",       # Подчёркивание
    "blink": "5",           # Мерцание (поддержка зависит от терминала)
    "reverse": "7",         # Инверсия цветов
    "hidden": "8"           # Скрытый текст
}

class __ANSI_Code:
    __start = "\033["
    __end = "\033[0m"

    def __init__(self, code):
        self.__code = int(code).__str__()

    def __stock(self, obj):
        return self.__start + self.__code + "m" + obj + self.__end

    def __exists(self, obj):
        return obj.replace("m", f";{self.__code}m", count=1)

    def __add__(self, obj):
        if isinstance(obj, str):
            return self.__stock(obj)
        return NotImplemented

    def __radd__(self, obj):
        if isinstance(obj, str) and self.__start in obj:
            return self.__exists(obj)
        elif isinstance(obj, str):
            return self.__stock(obj)
        return NotImplemented
        

