# Пространство имен != Области видимости.
# LEGB: Local <- Enclosing <- Global <- Built-in
from communicate import get_username, get_password

data_base =[]


def delete_user():
    pass


def create_user():
    username = get_username()
    password = get_password()

    user = username, password
    data_base.append(user)


create_user()
print(data_base)