DOG_COEFFICIENT = 10.5

age = int(input('Enter age: '))

if age <= 0:
    print('Incorrect input. Age must be > 0')
elif 1 <= age <= 2:
    dog_age = age * DOG_COEFFICIENT

    print(f'Dog age is {dog_age}')
else:
    dog_age = 2 * DOG_COEFFICIENT + (age - 2) * 4

    print(f'Dog age is {dog_age}')
