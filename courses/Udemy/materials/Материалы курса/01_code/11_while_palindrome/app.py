palindrome = 'racecar'

is_palindrome = palindrome == palindrome[::-1]
print(is_palindrome)


i = 0
j = len(palindrome) - 1
is_palindrome = True

while i < j:
    if palindrome[i] != palindrome[j]:
        is_palindrome = False
        break

    i += 1
    j -= 1

print(is_palindrome)
