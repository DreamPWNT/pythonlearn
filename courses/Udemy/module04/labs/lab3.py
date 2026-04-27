pattern = 'aeyuio'

player1_scores = 0
player2_scores = 2
player_order = 0

while True:
    if player_order == 0:
        print('Welcome to wolves game!')

        player_order = 1

    word = input(f'Player {player_order} enter your word: ')

    if word == 'exit':
        print(f'Player {player_order} want to stop game. Bye!')

        break

    wolves_quantity = 0
    count = 0

    while count < len(word):
        char = word[count]

        if char in pattern:
            wolves_quantity += 1

        count += 1

    if player_order == 1:
        player1_scores = wolves_quantity
    else:
        player2_scores = wolves_quantity

    if player_order == 1:
        player_order = 2
    else:
        print(
            f'Player 1 has {player1_scores} scores, Player 2 has {player2_scores} scores')

        if player1_scores == player2_scores:
            print('Nobody won the draw')
        else:
            print(
                f'Congratulation player {1 if player1_scores > player2_scores else 2}! You win!')

        player_order = 1
        player1_scores = 0
        player2_scores = 0
