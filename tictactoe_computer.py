"""
Tic Tac Toe -- human against computer
https://code.activestate.com/recipes/578905-tic-tac-toe/
"""
import random

new = [None] * 9
man = None
machine = None


def sign(man, machine):
    man = input("What team you want to be? X or O ").upper()
    while man not in ['X', 'O']:
        print("Invalid choice!")
        man = input("What team you want to be? X or O ").upper()
    if man == 'X':
        print("Ok, X is yours!")
        machine = 'O'
    else:
        print("Ok, O is yours!")
        machine = 'X'
    return man, machine


def decide_turn():
    while True:
        turn = input("Do you want to go first? (Y or N) ").upper()
        if turn not in ['Y', 'N']:
            continue
        return turn == 'Y'


def draw(a):
    """Draw the board"""
    board = """
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    """
    seats = [c if c else ' ' for c in a]
    print(board.format(*seats))


def congo_man():
    print("You won!")


def congo_machine():
    print("Computer won!")


def man_first(man, machine, new):
    while not win(man, machine, new):
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
        if win(man, machine, new):
            break
        print("Ummmm.... I'll take... ", end='')
        p_move = machine_move(man, machine, new)
        print(p_move)
        new[int(p_move)] = machine
        draw(new)
    q = win(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print("No-one wins. Tie.")


def machine_first(man, machine, new):
    while not win(man, machine, new):
        print("I'll take...")
        p_move = machine_move(man, machine, new)
        print(p_move)
        new[p_move] = machine
        draw(new)
        if win(man, machine, new):
            break
        move = man_move(man, new)
        new[int(move)] = man
        draw(new)
    q = win(man, machine, new)
    if q == 1:
        congo_man()
    elif q == 0:
        congo_machine()
    else:
        print("No-one wins. Tie.")


def win(man, machine, new):
    solutions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for i in solutions:
        if new[i[0]] and new[i[0]] == new[i[1]] == new[i[2]]:
            winner = new[i[0]]
            if winner == man:
                return 1
            elif winner == machine:
                return 0
            if None not in new:
                return 'TIE'
    if None not in new:
        return 'TIE'
    return None


def man_move(man, new):
    while True:
        slot = input("Where you want to move? (0..8) ")
        try:
            slot = int(slot)
        except ValueError:
            continue
        if slot not in range(9):
            continue
        if new[slot]:
            print("Sorry, the slot is already taken")
            continue
        return slot


def machine_move(man, machine, new):
    blank = []
    for i in range(9):
        if not new[i]:
            blank.append(i)

    for i in blank:
        new[i] = machine
        if win(man, machine, new) is 0:
            return i
        new[i] = None

    for i in blank:
        new[i] = man
        if win(man, machine, new) is 1:
            return i
        new[i] = None

    return int(blank[random.randrange(len(blank))])


def display_instruction():
    """Display game instructions"""
    print(
        """
        Welcome to the Game...
        You will make your move known by entering a number, 0 - 8.
        The will correspond to the board position as illustrated:

                          0 | 1 | 2
                         -----------
                          3 | 4 | 5
                         -----------
                          6 | 7 | 8

        Prepare yourself, the ultimate bettel is about to begin.....
        """)


def main(man, machine, new):
    display_instruction()
    print("Lets begin...")
    a = sign(man, machine)
    man = a[0]
    machine = a[1]
    b = decide_turn()
    if b == 1:
        print("You start!")
        print("Let's get started, here's a new board!")
        draw(new)
        man_first(man, machine, new)
    elif b == 0:
        print("I'll start!")
        print("Let's go...")
        draw(new)
        machine_first(man, machine, new)


if __name__ == "__main__":
    main(man, machine, new)
