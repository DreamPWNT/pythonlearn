word = input("Enter guessed word: ")
word_mask = len(word) * '_'

print('Welcome to word guessing game!')
print(f'Word to guess - {word_mask}')

while True:
    guessed_letter = input('Enter guessed letter: ')

    if guessed_letter in word:
        print(
            f'Congratulation, letter \'{guessed_letter}\' is in the guessed word!')

        index = 0

        while index < len(word_mask):
            if word[index] == guessed_letter:
                word_mask = (word_mask[0:index] +
                             guessed_letter + word_mask[index + 1:])

            index += 1

        print(f'Word to guess - {word_mask}')
    else:
        print(f'No :( letter \'{guessed_letter}\' is not in the guessed word')

    if word_mask == word:
        print('Your win!')

        break
