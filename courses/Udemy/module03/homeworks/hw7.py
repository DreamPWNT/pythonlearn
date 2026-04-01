# выдуманный адрес почты который создал юзер
gmail_user_email = "nobodyknowsmyage92@gmail.com"

# Нужно создать для него автоматически почты на других потовых серверах.
# У почтовых серверов домены это то что после символа @.

# Извлеките при помощи индексов и срезов из gmail_user_email
# почту пользователя "nobodyknowsmyage92" (индекс определите через
# метод строк index). И создайте для него почты на таких серверах:

outlook_domain = "@outlook.com"
proton_mail_domain = "@proton.me"

outlook_user_email = gmail_user_email[0:gmail_user_email.index(
    '@')] + outlook_domain
proton_user_email = gmail_user_email[0:gmail_user_email.index(
    '@')] + proton_mail_domain

# результат должен быть в этих переменных:
print(outlook_user_email)  # nobodyknowsmyage92@outlook.com
print(proton_user_email)  # nobodyknowsmyage92@proton.me
