possible_bits = ['0', '1']

bits = input("Enter input bit string (8 ltngth):")

while (bits != ''):
    if len(bits) != 8:
        print("Only length 8!!!")

        bits = input("Enter input bit string (8 length):")

        continue
    else:
        is_wrong_symbol = False

        for bit in bits:
            if bit not in possible_bits:
                print("Bit string must consist only '0' or '1'")

                bits = input("Enter input bit string (8 length):")

                is_wrong_symbol = True

                break

        if is_wrong_symbol:
            continue

        print(f"Bit evenness is {1 if not bits.count('1') % 2 else 0}")

    bits = input("Enter input bit string (8 length):")
