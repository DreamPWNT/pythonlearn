import math

EARTH_RADIUS = 6371.01

g1 = int(input('Enter first latitude value: '))
t1 = int(input('Enter first longitude value: '))
g2 = int(input('Enter second latitude value: '))
t2 = int(input('Enter second longitude value: '))

g1_rad = math.radians(g1)
t1_rad = math.radians(t1)
g2_rad = math.radians(g2)
t2_rad = math.radians(t2)

distance = round(EARTH_RADIUS *
                 math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)
                           * math.cos(t2)*math.cos(g1 - g1)), 2)

print(f'Distance between ({g1, t1}) and ({g2, t2}) = {distance}')
