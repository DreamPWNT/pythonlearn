estimations = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

total = 0.0
counter = 0
estimate = input("Enter estimate: ")

while estimate != '':
    total += float(estimations[estimate])
    counter += 1

    estimate = input("Enter estimate: ")

if counter == 0:
    print("No entered estimates...")
else:
    print(f"Average estimate: {round(total / counter, 2)}")
