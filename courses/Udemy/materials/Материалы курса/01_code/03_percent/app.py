value = float(input("Value: "))
part = float(input("How many?: "))

if value <= 0 or part < 0:
    print("Values cant be 0 or less than 0")

else:
    percent = part / value * 100
    print(round(percent, 2), "%")
