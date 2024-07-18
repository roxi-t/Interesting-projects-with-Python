from termcolor import colored

# Initialize the game board
board = list(range(1, 10))

# Possible winning combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# Preferred moves order
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))

def print_board():
    for i, cell in enumerate(board):
        end = " "
        if (i + 1) % 3 == 0:
            end = "\n\n"
        if cell == "X":
            print(colored(f"[{cell}]", "red"), end=end)
        elif cell == "O":
            print(colored(f"[{cell}]", "blue"), end=end)
        else:
            print(f"[{cell}]", end=end)

def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False

def can_move(brd, mve):
    return 1 <= mve <= 9 and isinstance(brd[mve - 1], int)

def is_winner(brd, plyr):
    for tup in winners:
        if all(brd[j] == plyr for j in tup):
            return True
    return False

def has_empty_space():
    return any(isinstance(cell, int) for cell in board)

def computer_move():
    mv = -1
    # Check if the computer can win
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break
    # Block the player if they are about to win
    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break
    # Make a preferred move
    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break
    return make_move(board, computer, mv)

player, computer = "X", "O"
print("Player: X\nComputer: O\n")

while has_empty_space():
    print_board()
    move = int(input("Choose your move (1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid move! Try again!")
        continue
    if won:
        print_board()
        print(colored("You Won!", "green"))
        break
    if computer_move()[1]:
        print_board()
        print(colored("You Lose!", "yellow"))
        break
else:
    print_board()
    print("It's a tie!")
