age = 13

if 0 <= age < 13:
    result = "Ребенок " + str(age)
elif 13 <= age < 18:     # Проверяется только если if False
    result = "Подросток " + str(age)
elif 18 <= age < 150:    # Проверяется только если прошлый elif False
    result = "Взрослый " + str(age)
else:                    # Выполняется только если все if-elif False
    result = "Возраст не может быть " + str(age)

print(result)
