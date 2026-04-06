length = float(input('Enter room length in foots (float format): '))
width = float(input('Enter room width in foots (float format): '))
area = round(length * width) / 43560

print(f'Area of room with length {length} and width {width} in acres = {area}')
