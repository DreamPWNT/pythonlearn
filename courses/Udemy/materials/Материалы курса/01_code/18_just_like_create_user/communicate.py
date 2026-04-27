import random
import string

from validators import (
    validate_username,
    validate_password
)


SYMBOLS_FOR_PASSWORD = string.ascii_letters + string.digits + string.punctuation


def generate_password():
    password = ""

    for _ in range(8):
        password += random.choice(SYMBOLS_FOR_PASSWORD)
    return password


def get_username():
    prompt = "Введите имя пользователя:\n"

    while True:
        username = input(prompt)
        prompt, status = validate_username(username)
        if status:
            break
    return username


def get_password():
    prompt = "Введите пароль пользователя или yes для генерации:\n"

    while True:
        password = input(prompt)
        if password == "yes":
            password = generate_password()
            break
        prompt, status = validate_password(password)
        if status:
            break

    return password
