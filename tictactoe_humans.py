"""
Tic Tac Toe game.
https://code.activestate.com/recipes/578816-the-game-of-tic-tac-toe-in-python/
"""


def print_board(board):
    """Displays the board"""
    print("The board looks like this:")
    print()

    for i in range(3):
        print(" ", end=' ')
        for j in range(3):
            if board[i * 3 + j] == 1:
                print('X', end=' ')
            elif board[i * 3 + j] == 0:
                print('O', end=' ')
            elif board[i * 3 + j] != -1:
                print(board[i * 3 + j] - 1, end=' ')
            else:
                print(' ', end=' ')

            if j != 2:
                print(" | ", end=' ')
        print()

        if i != 2:
            print("-----------------")
        else:
            print()


def print_instruction():
    """Prints out playing instructions"""
    print("Please use the following cell numbers to make your move")
    print_board([2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_input(turn):
    """Interactively get the next move from a user"""

    while True:
        user = input("Where would you like to place %s (1-9)? " % turn)
        try:
            user = int(user)
        except ValueError:
            print("%s is not a valid move! Please try again." % user)
            print()
            continue

        if not 1 <= user <= 9:
            print("That is not a valid move! Please try again.")
            print()
            print_instruction()
            continue

        return user - 1


def check_win(board):
    """Verifies whether there is a winner"""
    win_cond = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    for each in win_cond:
        try:
            if board[each[0] - 1] == board[each[1] - 1] and \
                    board[each[1] - 1] == board[each[2] - 1]:
                return board[each[0] - 1]
        except IndexError:
            pass
    return -1


def quit_game(board, msg):
    """Ends the game"""
    print_board(board)
    print(msg)
    quit()


def main():
    """
    1. setup game
    2. alternate turns
    3. check if win or end
    4. quit and show the board
    """
    print_instruction()

    board = []
    for _ in range(9):
        board.append(-1)

    win = False
    move = 0
    while not win:

        # print(board)
        print_board(board)
        print("Turn number %s" % (move + 1))
        if move % 2 == 0:
            turn = 'X'
        else:
            turn = 'O'

        # get user input
        user = get_input(turn)
        while board[user] != -1:
            print("Invalid move! Cell already taken. Please try again.")
            print()
            user = get_input(turn)
        board[user] = 1 if turn == 'X' else 0

        # advance move and check for end game
        move += 1
        if move > 4:
            winner = check_win(board)
            if winner != -1:
                out = "The winner is "
                out += "X" if winner == 1 else "O"
                out += " :)"
                quit_game(board, out)
            elif move == 9:
                quit_game(board, "No winner :(")


if __name__ == "__main__":
    main()
