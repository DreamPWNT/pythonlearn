HEX_CHARS = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def number_to_system(n, foundation=2):
    result = ""

    if n < foundation:
        if foundation != 16:
            return n
        else:
            return n if n < 10 else HEX_CHARS[n]

    while n >= foundation:
        quotient = n // foundation

        if foundation != 16:
            result += str(n % foundation)
        else:
            result += (
                str(n % foundation)
                if n % foundation < 10
                else HEX_CHARS[n % foundation]
            )

        n = quotient

    if n != 0:
        if foundation != 16:
            result += str(n)
        else:
            result += str(n) if n < 10 else HEX_CHARS[n]

    return result[::-1]


n = 18765

print(number_to_system(n, 2))
print(number_to_system(n, 8))
print(number_to_system(n, 16))
