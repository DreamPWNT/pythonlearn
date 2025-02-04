english_alphabet = list("abcdefghijklmnopqrstuvwxyz")
russian_alphabet = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")

alphabet_choice = 0
alphabet = english_alphabet
step = 3


def crypt(value, alphabet, step):
    max_ord = len(alphabet)
    crypted_value = ""

    for ch in value:
        if not ch.isalpha():
            crypted_value += ch
            continue
        else:
            alphabet_idx = alphabet.index(ch.lower())

        if alphabet_idx + step >= max_ord:
            delta_step = step - (max_ord - alphabet_idx)
            crypted_value += (
                alphabet[delta_step]
                if not ch.isupper()
                else alphabet[delta_step].upper()
            )
        else:
            crypted_value += (
                alphabet[alphabet_idx + step]
                if not ch.isupper()
                else alphabet[alphabet_idx + step].upper()
            )

    return crypted_value


def decrypt(value, alphabet, step):
    min_ord = 1
    max_ord = len(alphabet)
    decrypted_value = ""

    for ch in value:

        if not ch.isalpha():
            decrypted_value += ch
            continue
        else:
            alphabet_idx = alphabet.index(ch.lower())

        if alphabet_idx < step:
            delta_step = max_ord - (step - alphabet_idx)
            decrypted_value += (
                alphabet[delta_step]
                if not ch.isupper()
                else alphabet[delta_step].upper()
            )
        else:
            decrypted_value += (
                alphabet[alphabet_idx - step]
                if not ch.isupper()
                else alphabet[alphabet_idx - step].upper()
            )

    return decrypted_value


"""
alphabet_choice = int(input("Введите тип алфавита (0 - английский, 1 - русский): "))

if alphabet_choice != 0 and alphabet_choice != 1:
    print("Некорректный выбор алфавита, до свидания!")
else:
    if alphabet_choice == 0:
        alphabet = english_alphabet
    else:
        alphabet = russian_alphabet

    crypt_type = int(input("Введите тип шифрования (0 - шифровка, 1 - дешифровка): "))

    if crypt_type != 0 and crypt_type != 1:
        print("Некорректный выбор типа шифрования, до свидания!")
    else:
        step = int(input("Введите шаг алгоритма: "))

        if step >= len(alphabet):
            print("Некорректный шаг. Щаг должен быть максимум", len(alphabet))
        else:
            print("Введите строку для применения алгоритма")

            S = input()

            if crypt_type == 0:
                result = crypt(S, alphabet, step)
            else:
                result = decrypt(S, alphabet, step)

            print("Строка после применения алгоритма:")
            print(result)
"""


def to_only_chars(S):
    result = ""

    for ch in S:
        if ch.isalpha():
            result += ch

    return result


L = 'Day, mice. "Year" is a mistake!'.split()
print(L)
result = []

for word in L:
    result.append(crypt(word, "abcdefghijklmnopqrstuvwxyz", len(to_only_chars(word))))

print(*result)
