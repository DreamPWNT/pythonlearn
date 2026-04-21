from sys import getsizeof

all_nums = [-3, 1, 0, 10, -20, 5]
dct = {}
absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))

print(absolute_nums)
print(all_nums)

absolute_nums = [abs(num) for num in all_nums]

print(absolute_nums)

positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)

print(positive_nums)

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)

my_set = {1, 10, 15}
new_set = set()

new_set = {val * val for val in my_set}

print(new_set)

my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10

print(my_scores)
print(scores)

scores = {k: v * 10 for k, v in my_scores.items()}
scores_set = {v * 10 for k, v in my_scores.items()}
scores_list = [v * 10 for k, v in my_scores.items()]

print(scores)
print(scores_set)
print(scores_list)

my_scores = [10, 7, 34]

scores = {k: v for k, v in enumerate(my_scores)}

print(scores)


nums = (3, 5, 10)

squares = (num * num for num in nums)

print(squares)

squares = (num * num for num in range(6))

print(squares)
print(type(squares))
print(next(squares))


for num in squares:
    print(num)

squares_gen = (num * num for num in range(10000))

print(getsizeof(squares_gen))
print(type(squares_gen))

squares_list = [num * num for num in range(10000)]

print(getsizeof(squares_list))
print(type(squares_list))
