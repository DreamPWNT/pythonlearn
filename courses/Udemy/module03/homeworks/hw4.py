# Возможные ТРИ варианта входных данных:
# 'https://www.example.com'
# 'www.example.com'
# 'example.com'

# Переменная url (переименовать нельзя).
# Для проверки случаев меняйте значения в переменной.
url = 'example.com'

if not 'https://' in url:
    if not 'www.' in url:
        url = 'https://www.' + url
    else:
        url = 'https://' + url

# Переменная url должна содержать нормальный url:
print(url)
