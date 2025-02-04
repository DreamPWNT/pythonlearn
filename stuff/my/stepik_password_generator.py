import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "#$%&*+-=?@^_."
ambigious = "il1Lo0O"


def get_conditions():
    chars = ""

    if input("Использовать цифры? ") == "да":
        chars += digits
    if input("Использовать строчные буквы? ") == "да":
        chars += lowercase_letters
    if input("Использовать заглавные буквы? ") == "да":
        chars += uppercase_letters
    if input("Использовать спецсимволы? ") == "да":
        chars += punctuation

    if input("Убрать неоднозначные последовательности? ") == "да":
        chars = list(chars)

        for ch in ambigious:
            chars.remove(ch)

        chars = "".join(chars)

    return chars


def generate_password(length, alphabet):
    return "".join(random.sample(alphabet, length))


def init():
    result = []

    passwords_quantity = int(input("Введите количество паролей для генерации: "))
    password_length = int(input("Введите длину для каждого пароля: "))

    alphabet = get_conditions()

    for _ in range(passwords_quantity):
        result.append(generate_password(password_length, alphabet))

    print("Ваши пароли:\n", *result, sep="\n")


init()
