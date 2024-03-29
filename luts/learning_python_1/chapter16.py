import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
counter = 0
n = len(lst_in)

while counter < n:
    print(counter)

    counter += 1

print(*lst_in)
