# madam, racecar, mom, noon

# Имя переменой word не менять! В нем строка слова для проверки.
# Значения в нем менять можно!
word = 'level1'

if word == word[-1::-1]:
    is_palindrome = True
else:
    is_palindrome = False

str = list(word)
str.reverse()
print(list(word).reverse())
print(str)
print(list(word).reverse().split())
# Не мухлевать!
# В переменной is_palindrome должно быть True если палиндром
# или False если нет.
print(is_palindrome)
