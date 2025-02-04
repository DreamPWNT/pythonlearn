import random

word_list = [
    "водка",
    "селёдка",
    "хуета",
    "рачьё",
    "пушистина",
    "кумурблиска",
    "хрумка",
    "тайлер",
    "интеграл",
    "декоратор",
    "пайтон",
    "хуяйтон",
    "сигарета",
    "рюмочка",
    "лоцманьё",
    "сосиска",
    "мисьё",
]


def get_word(word_list):
    return random.choice(word_list)


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def is_valid(word):
    return True if word.isalpha() else False


def play(word):
    print(f"DEBUG: {word}")
    word_completion = "_" * len(
        word
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))

    while tries > 0:
        print("Слово:", word_completion)

        s = input("Введите слово или букву: ")

        if not is_valid(s):
            print("Неправильный ввод. Должна быть либо 1 буква или слово")
            continue
        else:
            if len(s) > 1:
                if s in guessed_words:
                    print(
                        "Вы уже называли это слово, выберите другое слово или назовите букву"
                    )
                    continue

                if word == s:
                    print(f"Вы угадали! Молодец! Это слово: {word}")
                    break

                    guessed_words.append(s)
                else:
                    tries -= 1

                    if tries != 0:
                        print(
                            f"Неверное слово, попробуйте ещё раз. Осталось попыток {tries}"
                        )
                        print(display_hangman(tries))

                        guessed_words.append(s)
            else:
                if s in guessed_letters:
                    print(
                        "Вы уже называли букву, выберите другую букву или назовите слово"
                    )
                    continue

                if s in word:
                    print(f"Верно! Открываем букву {s}")

                    word_list = list(word)
                    word_completion_list = list(word_completion)

                    for i in range(len(word_list)):
                        if word_list[i] == s:
                            word_completion_list[i] = s

                    word_completion = "".join(word_completion_list)

                    if word_completion == word:
                        print(f"Вы угадали! Молодец! Это слово: {word}")
                        break

                    guessed_letters.append(s)
                else:
                    tries -= 1

                    if tries != 0:
                        print(
                            f"Неверная буква, попробуйте ещё раз. Осталось попыток {tries}"
                        )
                        print(display_hangman(tries))

                        guessed_letters.append(s)

        if tries == 0:
            print(f"Извините, вы проиграли... Слово было: {word}")


play(get_word(word_list))
