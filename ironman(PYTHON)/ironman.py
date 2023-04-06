import random
import time
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

pieces = {
    "red": [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ],
    "green": [
        [7, 0],
        [7, 1],
        [8, 0],
        [8, 1]
    ],
    "yellow": [
        [0, 7],
        [0, 8],
        [1, 7],
        [1, 8]
    ],
    "blue": [
        [7, 7],
        [7, 8],
        [8, 7],
        [8, 8]
    ]
}
def roll_dice():
    input("Press enter to roll the dice...")
    time.sleep(1)
    dice = random.randint(1, 6)
    print("You rolled a " + str(dice))
    return dice
def move_piece(piece, steps):
    current_row = piece[0]
    current_col = piece[1]
    current_value = board[current_row][current_col]
    board[current_row][current_col] = 0
    new_row = current_row
    new_col = current_col
    if current_value == 0:
        if steps == 6:
            new_value = 1
            print("You can move out of the starting point!")
        else:
            new_value = 0
            print("You need a 6 to move out of the starting point!")
    else:
        new_value = current_value + steps
        if new_value > 56:
            new_value = current_value
            print("You cannot move beyond the end point!")
        else:
            print("You moved " + str(steps) + " steps.")
            if new_value == 56:
                print("You have reached the end point!")
            else:
                if new_value % 8 == 0:
                    new_row 
