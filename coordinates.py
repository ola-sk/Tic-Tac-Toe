from typing import List
from time import sleep
from board import is_board_full


def get_human_coordinates(board, current_player):
    """
    Should return the read coordinates for the tic tac toe board from the terminal.
    The coordinates should be in the format letter, number where the letter is
    A, B or C and the number 1, 2 or 3.
    If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf)
    than a warning message should appear and the coordinates reading process repeated.
    If the user enters a coordinate that is already taken on the board.
    than a warning message should appear and the coordinates reading process repeated.
    If the user enters the word "quit" in any format of capitalized letters the program
    should stop.
    """
    # letter = ""
    # number = 0
    # while ((letter != "A" and letter != "B" and letter != "C") or (number != 1 and number != 2 and number != 3)):
    #     letter = input("Enter a line A, B or C: ")
    #     if "quit" == letter.lower(): 
    #     print("Good Bye")
    #     break

    # number = input("Enter a column 1, 2 or 3: ")

    # if "quit" == number.lower():
    #     print("Good Bye")
    #     break

    # number = int(number)
    # if ((letter != "A" and letter != "B" and letter != "C") or (number != 1 and number != 2 and number != 3)):
    #     print("Warning! Invalid input!")
    # else:
    #     print(f"You have chosen {letter}{number} ")
    #     return letter, number

    import sys
    field = ''
    fields = {
        "A1": board[0][0],
        "A2": board[0][1],
        "A3": board[0][2],
        "B1": board[1][0],
        "B2": board[1][1],
        "B3": board[1][2],
        "C1": board[2][0],
        "C2": board[2][1],
        "C3": board[2][2]
    }

    while (
            field != "A1" and field != "A2" and field != "A3" and field != "B1" and field != "B2" and field != "B3" and
            field != "C1" and field != "C2" and field != "C3") or \
            fields[field] != ".":
        field = input(f"{current_player[0]}, enter a field A1, A2, A3, B1, B2, B3, C1, C2 or C3: ")

        if field.lower() == "quit":
            sys.exit()

        if (field != "A1" and field != "A2" and field != "A3" and field != "B1" and field != "B2" and field != "B3" and
                field != "C1" and field != "C2" and field != "C3"):
            print("Warning! Invalid input!")
        elif fields[field] != ".":
            print("Sorry. The field is already taken, try again!")
        else:
            letter = field[0]
            number = int(field[1])
            return letter, number

    # letter = input("Enter a row letter (A/B/C): ")
    # while letter.upper() != "A" and letter.upper() != "B" and letter.upper() != "C":
    #     print("Your input was incorrect!")
    #     letter = input("Choose a row A, B or C: ")
    # else:
    #     try:
    #         number = int(input("Please choose a column 1, 2 or 3: "))
    #     except ValueError:
    #         pass
    #     while number != 1 and number != 2 and number != 3:
    #         print("Incorrect input!")
    #         try:
    #             number = int(input("Choose a column 1, 2 or 3: "))
    #         except ValueError:
    #             print("Please enter a number character!")
    #     else:
    #         return letter, number


def convert_human_coordinates(human_coordinates: tuple):
    x, y = human_coordinates
    # x should be a letter representing a row on the board.
    # y should be a number representing a column on the board.
    try:
        if x.lower() == 'a':
            x = 0
        elif x.lower() == 'b':
            x = 1
        elif x.lower() == 'c':
            x = 2
        else:
            raise ValueError
        if y == 1:
            y = 0
        elif y == 2:
            y = 1
        elif y == 3:
            y = 2
        else:
            raise ValueError
    except ValueError:
        print("The coordinates that the function `convert_human_coordinates()` got are incorrect. Please debug.")
    return x, y


def get_random_ai_coordinates(board):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) then "None"
    should be returned.
    """
    from random import seed
    from random import choice
    from board import get_empty_fields
    empty_fields: set = get_empty_fields(board)
    if is_board_full(board, empty_fields):
        return None
    else:
        seed()
        coordinate = choice(list(empty_fields))
        sleep(1)
        return coordinate

    # check if coordinate is free...
    # 1st option:
    # keep track of all coordinates that are free vs taken and update both of them when the state changes.
    # In this option we would need to pass to the function the free coordinates of the board and once we draw the
    # coordinates, we would need to deal with updating the board as well.
    # 2nd option:
    # choose a coordinate randomly in a loop, as soon as they are free, return the coordinates.
    #
    # return x, y


def get_unbeatable_ai_coordinates(board):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    The chosen coordinate should always stop the other player from winning or
    maximize the current player's chances to win.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """
    pass


def perform_move(board_local, row_coordinate, column_coordinate, current_player):
    board_local[row_coordinate][column_coordinate] = current_player
    return board_local


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    board_1: list[list[str]] = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    print("It should print the coordinates selected by the human player")
    print(get_human_coordinates(board_1, 'X'))

    board_2: list[list[str]] = [
        ["O", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2))

    board_3: list[list[str]] = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3))

    board_4: list[list[str]] = [
        [".", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should always be (0, 0)--------------")
    # print(get_unbeatable_ai_coordinates(board_4, "X"))

    board_5: list[list[str]] = [
        ["X", "O", "."],
        ["X", ".", "."],
        ["O", "O", "X"],
    ]
    print("The printed coordinate should always be (1, 1)----------------")
    # print(get_unbeatable_ai_coordinates(board_5, "O"))

    board_6: list[list[str]] = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("The printed coordinate should either (0, 2) or (2, 0)--------------------")
    # print(get_unbeatable_ai_coordinates(board_6))
