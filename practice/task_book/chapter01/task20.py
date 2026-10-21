UNIVERSAL_GAS_CONSTANT = 8.314
KELVIN_OEFFICIENT = 273.15

P = int(input('Enter pressure in Pascals: '))
V = int(input('Enter volume in litres: '))
T = int(input('Enter temperature in Celsius: '))

n = ((P * V) / (UNIVERSAL_GAS_CONSTANT * (T + KELVIN_OEFFICIENT)))

print(f'Substance quantity = {n}')
