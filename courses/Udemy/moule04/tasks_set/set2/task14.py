arr = [10, 100, 500, 11, 18, 99, -3, 101]

print(max(arr))
print(min(arr))
print(sum(arr))
print(round(sum(arr) / len(arr), 2))

arr_max = arr[0]
arr_min = arr[0]
arr_sum = 0
arr_count = 0

for item in arr:
    if item > arr_max:
        arr_max = item

    if item < arr_min:
        arr_min = item

    arr_sum += item
    arr_count += 1

print(arr_max, arr_min, arr_sum, round(arr_sum / arr_count, 2))
