import timer1
import timeit

reps, text = 100_000, 'hack' * 100

print(timer1.once(pow, 2, 1000)[0])
print(timer1.once(str.upper, text)[0])
print(timer1.total(reps, pow, 2, 1000)[0])
print(timer1.total(reps, str.upper, text)[0])
print(timer1.bestof(50, pow, 2, 1000)[0])
print(timer1.bestof(50, str.upper, text)[0])
print(timer1.bestoftotal(50, reps, pow, 2, 1000)[0])
print(timer1.bestoftotal(50, reps, str.upper, text)[0])

print(
    min(timeit.repeat(stmt='[x ** 2 for x in range(1000)]', number=1000, repeat=5)))

X = 1


def func():
    global X
    X = 121


print(X)
