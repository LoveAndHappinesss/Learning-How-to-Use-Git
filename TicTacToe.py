def display_board(choice, turn, board_position):

    if turn == 'X':

        board_position[choice] = 'X'

    else:

        board_position[choice] = 'O'

    print('\n')
    print('  '+board_position[0]+'  |  '+board_position[1]+'  |  '+board_position[2]+'  ')
    print(' ------------')
    print('  '+board_position[3]+'  |  '+board_position[4]+'  |  '+board_position[5]+'  ')
    print(' ------------')
    print('  '+board_position[6]+'  |  '+board_position[7]+'  |  '+board_position[8]+'  ')
    print('\n')

    return board_position


def win_check(player1, player2, game_turn):

    winner = False

    if player1 == 'X':

        if (board_position[0] == "X" and board_position[1] == 'X'
            and board_position[2] == 'X' or board_position[3] == "X"
            and board_position[4] == 'X' and board_position[5] == 'X'
            or board_position[6] == "X" and board_position[7] == 'X'
            and board_position[8] == 'X' or board_position[0] == "X"
            and board_position[3] == 'X' and board_position[6] == 'X'
            or board_position[1] == "X" and board_position[4] == 'X'
            and board_position[7] == 'X' or board_position[2] == "X"
            and board_position[5] == 'X' and board_position[8] == 'X'
            or board_position[0] == "X" and board_position[4] == 'X'
            and board_position[8] == 'X' or board_position[2] == "X"
           and board_position[4] == 'X' and board_position[6] == 'X'):

            winner = True
            print("Congratulations! Player 1 has won the game!")

        if (board_position[0] == "O" and board_position[1] == 'O'
            and board_position[2] == 'O' or board_position[3] == "O"
            and board_position[4] == 'O' and board_position[5] == 'O'
            or board_position[6] == "O" and board_position[7] == 'O'
            and board_position[8] == 'O' or board_position[0] == "O"
            and board_position[3] == 'O' and board_position[6] == 'O'
            or board_position[1] == "O" and board_position[4] == 'O'
            and board_position[7] == 'O' or board_position[2] == "O"
            and board_position[5] == 'O' and board_position[8] == 'O'
            or board_position[0] == "O" and board_position[4] == 'O'
            and board_position[8] == 'O' or board_position[2] == "O"
                and board_position[4] == 'O' and board_position[6] == 'O'):

            winner = True
            print("Congratulations! Player 2 has won the game!")

    elif player1 == 'O':

        if (board_position[0] == "X" and board_position[1] == 'X'
            and board_position[2] == 'X' or board_position[3] == "X"
            and board_position[4] == 'X' and board_position[5] == 'X'
            or board_position[6] == "X" and board_position[7] == 'X'
            and board_position[8] == 'X' or board_position[0] == "X"
            and board_position[3] == 'X' and board_position[6] == 'X'
            or board_position[1] == "X" and board_position[4] == 'X'
            and board_position[7] == 'X' or board_position[2] == "X"
            and board_position[5] == 'X' and board_position[8] == 'X'
            or board_position[0] == "X" and board_position[4] == 'X'
            and board_position[8] == 'X' or board_position[2] == "X"
                and board_position[4] == 'X' and board_position[6] == 'X'):

            winner = True
            print("Congratulations! Player 2 has won the game!")

        if (board_position[0] == "O" and board_position[1] == 'O'
            and board_position[2] == 'O' or board_position[3] == "O"
            and board_position[4] == 'O' and board_position[5] == 'O'
            or board_position[6] == "O" and board_position[7] == 'O'
            and board_position[8] == 'O' or board_position[0] == "O"
            and board_position[3] == 'O' and board_position[6] == 'O'
            or board_position[1] == "O" and board_position[4] == 'O'
            and board_position[7] == 'O' or board_position[2] == "O"
            and board_position[5] == 'O' and board_position[8] == 'O'
            or board_position[0] == "O" and board_position[4] == 'O'
            and board_position[8] == 'O' or board_position[2] == "O"
                and board_position[4] == 'O' and board_position[6] == 'O'):

            winner = True
            print("Congratulations! Player 1 has won the game!")

    elif game_turn == 9:

        winner = True
        print("The game is a draw")

    return winner


def p1_what_side():

    isvalid = False
    choice = ''

    while isvalid is False:

        choice = input("Player 1, would you like to be X or O: ").upper()

        if choice == 'X':

            isvalid = True
            print("Player 1 controls the Xs")

            return 'X'

        if choice == 'O':

            isvalid = True
            print("Player 1 controls the Os")

            return 'O'

        else:

            print("This is an invalid input. Please try again.")


def p2_what_side(x):

    if x == 'O':

        return 'X'

    else:

        return 'O'


def user_choice(turn):

    isvalid = False

    while isvalid is False:

        if turn == 'X':

            choice = int(input('Where would you like to place your X?: '))

        else:

            choice = int(input('Where would you like to place your O?: '))

        if choice not in occupied_spots and 0 < choice < 10:

            occupied_spots.append(choice)

            return (choice - 1)

        else:

            print("This is not a valid input. Please try again.")


def play_again():

    isvalid = False
    choice = ''

    while isvalid is False:

        choice = input('Would you like to play again (Y or N): ').upper()

        if choice == 'N':

            isvalid = True
            print("Thanks for playing!")

            return False

        if choice == 'Y':

            isvalid = True

            return True

        else:

            print("This is an invalid input. Please try again.")


play_game = True

while play_game is True:

    player1 = p1_what_side()
    player2 = p2_what_side(player1)
    turn = player1
    win = False
    game_turn = 0
    board_position = ['', '', '', '', '', '', '', '', '']
    occupied_spots = []

    while win is False:

        choice = user_choice(turn)
        display_board(choice, turn, board_position)
        win = win_check(player1, player2, game_turn)
        game_turn += 1

        if turn == player1:

            turn = player2

        else:

            turn = player1

    play_game = play_again()
