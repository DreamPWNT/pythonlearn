
def merge_lists_to_dict(list_1, list_2):
    merged_list = zip(list_1, list_2)

    return dict(merged_list)


L1 = ['a', 'b', 'c']
L2 = [3, 56, 8]

res = merge_lists_to_dict(L1, L2)

print(res)

print(merge_lists_to_dict(['name', 'language', 'job'], [
      'Vasisualiy', 'C++', 'coder!']))
