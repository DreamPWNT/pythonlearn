"""bytearray - изменяемый вариант bytes"""

# Нужен для того, чтоб можно было изменять саму "строку байтов" для
# каких либо преобразований.
# Содержит все методы bytes + дополнительные для возможности вносить изменения.

ba = bytearray('aaa', encoding='utf-8')  # bytearray(b'aaa')
# Или используя литерал b
ba = bytearray(b'aaa')  # bytearray(b'aaa')

ba.append(65)
print(ba)  # bytearray(b'aaaA')

ba.append(256)  # ValueError: byte must be in range 0 - до 256

ba.append('A')  # TypeError: 'str' object cannot be interpreted as an integer

# Методы bytesarray:

# Добавляет байт в конец массива.
ba = bytearray(b"abc")
ba.append(100)  # Добавляет байт с числом 100.
print(ba)  # bytearray(b'abcd')

# Расширяет массив, добавляя элементы из итерируемого объекта.
ba = bytearray(b"abc")
ba.extend([100, 101])
print(ba)  # bytearray(b'abcde')

# Вставляет байт на указанную позицию.
ba = bytearray(b"abc")
ba.insert(1, 100)  # Вставляет байт с числом 100 на позицию 1
print(ba)  # bytearray(b'adbc')

# Удаляет первое вхождение указанного байта.
ba = bytearray(b"abcabc")
ba.remove(97)  # Удаляет первый байт с числом 97 (буква 'a')
print(ba)  # bytearray(b'bcabc')

# Удаляет и возвращает байт по индексу (по умолчанию последний).
ba = bytearray(b"abc")
last = ba.pop()
print(last)  # 99 (символ 'c')
print(ba)  # bytearray(b'ab')

# Очищает массив.
ba = bytearray(b"abc")
ba.clear()
print(ba)  # bytearray(b'')

# Изменяет порядок байтов на обратный.
ba = bytearray(b"abc")
ba.reverse()
print(ba)  # bytearray(b'cba')

# Можно изменять содержимое массива с помощью срезов.
ba = bytearray(b"hello")
ba[0:2] = b"HI"
print(ba)  # bytearray(b'HIllo')
