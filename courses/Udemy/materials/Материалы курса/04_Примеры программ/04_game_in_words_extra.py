# Новые строки кода помечены #!!!

print("Добро пожаловать в игру в слова!")   #!!!

player1 = input('Имя игрока 1: ')           #!!!
player2 = input('Имя игрока 2: ')           #!!!

player1_scores = 0                          #!!!
player2_scores = 0                          #!!!

turn = player1                              #!!!

while True:                                 #!!!

    user_input = input(f"{turn}, введите слово (exit для выхода):\n>")

    if user_input == 'exit':                #!!!
        break                               #!!!

    vowels = "eyuioa"
    vowels_count = 0
    index = 0
    a_count = 0

    while index < len(user_input):
        char = user_input[index]
        index += 1

        if char in vowels:
            if char == "a" and a_count > 0:
                continue
            if char == "a":
                a_count += 1
            vowels_count += 1

        elif char == "t":
            break
    else:
        vowels_count += 1


    if turn == player1:                     #!!!
        print(f'{player1} - {vowels_count}')#!!!
        player1_scores += vowels_count      #!!!
        turn = player2                      #!!!
    else:                                   #!!!
        print(f'{player2} - {vowels_count}')#!!!
        player2_scores += vowels_count      #!!!
        turn = player1                      #!!!

print('Results')                            #!!!
print(f'{player1} - {player1_scores}\n{player2} - {player2_scores}')
    
