pascal_pressure = int(input('Enter pressure value in kilo Pascals: '))

POUNDS_COEFFICIENT = 0.1450377
MMS_COEFFICIENT = 7.500615
ATMOSPHERES_COEFFICIENT = 0.009869233

pounds_pressure = pascal_pressure * POUNDS_COEFFICIENT
mms_pressure = pascal_pressure * MMS_COEFFICIENT
atmosphere_pressure = pascal_pressure * ATMOSPHERES_COEFFICIENT

print(
    f'Pressure in pounds/sq_inch = {pounds_pressure}, in mercury/mm = {mms_pressure}, in atmospheres = {atmosphere_pressure}')
