COEFFICIENT_1 = 13.12
COEFFICIENT_2 = 0.6215
COEFFICIENT_3 = 11.37
COEFFICIENT_4 = 0.3965

t = int(input('Enter temperature: '))
v = int(input('Enter wind speed: '))

WCI = COEFFICIENT_1 + COEFFICIENT_2 * t - COEFFICIENT_3 * \
    pow(v, 0.16) + COEFFICIENT_4 * t * pow(v, 0.16)

print(f'WCI = {WCI}')
