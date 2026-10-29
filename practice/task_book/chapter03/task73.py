alphabet = 'abcdefghijklmnopqrstuvwxyz'

step = int(input("Enter a crypt step: "))
S = input("Enter a string: ")

for index, ch in enumerate(S, 0):
    is_upper_flag = ch.isupper()

    if not ch.isalpha():
        continue

    idx = alphabet.find(ch.lower())
    new_idx = idx + step

    if new_idx >= len(alphabet):
        new_idx = new_idx - len(alphabet)

    print(idx, new_idx)

    L = list(S)
    L[index] = alphabet[new_idx] if not is_upper_flag else alphabet[new_idx].upper()
    S = ''.join(L)

print(f"Crypted string is: {S}")
