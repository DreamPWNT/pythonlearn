a = 5
b = 3


def sum(a, b):
    c = a + b

    print(c)


sum(a, b)

a = 8
b = 12

sum(a, b)

print(type(sum))


def my_fn(a, b):
    a = a + 1
    c = a + b

    print(id(b))

    return c


res = my_fn(10, 3)

print(res)


def my_fn_2():
    pass


print(my_fn_2())

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)

print(res)
print(num_one)
print(id(num_two))


def increase_person_age(person):
    person_copy = person.copy()

    print(id(person))
    print(id(person_copy))

    person_copy['age'] += 1

    return person_copy


person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one))

increase_person_age(person_one)

print(person_one['age'])


def merge_lists_to_dict(list_1, list_2):
    merged_list = zip(list_1, list_2)

    return dict(merged_list)


L1 = ['a', 'b', 'c']
L2 = [3, 56, 8]

res = merge_lists_to_dict(L1, L2)

print(res)

print(merge_lists_to_dict(['name', 'language', 'job'], [
      'Vasisualiy', 'C++', 'coder!']))
