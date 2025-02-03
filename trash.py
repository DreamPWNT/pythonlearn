line = "Hello, my name is [u-1061][u-1072][u-1082][u-1080]!"
counter = 0

decrypted_line = ""
flag = True

for ch in line:
    if ch == "[":
        flag = False
        print(line[counter + 3 : counter + 7])
        decrypted_line += chr(int(line[counter + 3 : counter + 7]))
        print(decrypted_line)
    elif ch == "]":
        flag = True
    elif ch != "[" and ch != "]" and flag == True:
        decrypted_line += ch

    counter += 1

print(decrypted_line)

print(max("9", "10", "11"))

S = "Толстой А.Н., «Петр Первый»"

first_space = S.find(" ")
second_space = S.find(" ", first_space + 1)
last_name = S[0:first_space]
book_name = S[second_space + 1 :]
print(first_space, second_space, last_name, book_name)

print(10 % 2)

a = 100000
b = 22

a, b = b, a % b
print(a, b)
a, b = b, a % b
print(a, b)
a, b = b, a % b
print(a, b)

lst = None

print(lst is None)

lines = ["0 1 0\n", "0 0 0\n", "1 0 1\n"]
lst2D = [list(map(int, i.strip().split())) for i in lines]

N = len(lst2D[0])
print(N)


def verify(matrix):
    for row_idx in range(len(matrix)):
        for idx in range(len(matrix[row_idx])):
            print(idx)
            if matrix[row_idx][idx] == 1 and not is_isolate(matrix, idx, row_idx, N):
                return False

    return True


def is_isolate(matrix, idx, row_idx, N):
    print(matrix[row_idx])
    print(row_idx)
    if row_idx == 0:
        if (
            sum(matrix[row_idx][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 1
            or sum(matrix[row_idx + 1][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 0
        ):
            return False
    elif row_idx == N - 1:
        if (
            sum(matrix[row_idx][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 1
            or sum(matrix[row_idx - 1][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 0
        ):
            return False
    else:
        if (
            sum(matrix[row_idx][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 1
            or sum(matrix[row_idx - 1][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 0
            or sum(matrix[row_idx + 1][idx - 1 if idx - 1 >= 0 else 0 : idx + 2]) > 0
        ):
            return False

    return True


print(verify(lst2D))

# здесь продолжайте программу


def get_rec_N(N):
    if N > 1:
        get_rec_N(N - 1)

    print(N)


get_rec_N(8)


def get_rec_sum(L, idx=0, sum=0):
    if idx <= len(L) - 1:
        sum = sum + L[idx]

        return get_rec_sum(L, idx + 1, sum)
    else:
        return sum


print(get_rec_sum([1, 21, 65, 3, 65, 7]))


def fib_rec(N, f=[1, 1]):
    if N == 2 or len(f) == N:
        return f
    elif len(f) < N:
        return fib_rec(N, f + [f[-2] + f[-1]])


print(fib_rec(7))

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ["True", [-2, -1]]], 7.89]

# здесь продолжайте программу


def get_line_list(d, a=[]):
    l = len(d)

    if l == 0:
        return a
    elif type(d[0]) == list:
        tmp = get_line_list(d[0], a)
        return get_line_list(d[1:], a)
    else:
        a.append(d[0])
        return get_line_list(d[1:], a)


print(get_line_list(d))

L = [5, 3, 3, 6, 8, 5, 3, -10, 343, 53, 7]
print((len(L) / 2) + 1)

L1 = L[: (len(L) // 2)]
L2 = L[len(L) // 2 :]
L1.sort()
L2.sort()


print(L1, L2)


def merge_sort(L1, L2, result=None):
    if result == None:
        result = []

    if len(L1) != 0 and len(L2) != 0:
        if L1[0] < L2[0]:
            result.append(L1[0])

            return merge_sort(L1[1:], L2, result)
        elif L1[0] > L2[0]:
            result.append(L2[0])

            return merge_sort(L1, L2[1:], result)
        else:
            result.append(L1[0])

            return merge_sort(L1[1:], L2[1:], result)
    elif len(L1) == 0 and len(L2) > 0:
        result += L2

        return result
    elif len(L2) == 0 and len(L1) > 0:
        result += L1

        return result
    elif len(L1) == 0 and len(L2) == 0:
        return result


print(merge_sort(L1, L2))
