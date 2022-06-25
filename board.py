def get_empty_board():
    """
    Should return a list with 3 sub-lists.
    Each sublist should contain 3 time the "." character
    """
    board_0 = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ]
    return board_0


def get_empty_fields(board):
    """Returns coordinates of empty cells in the board. The coordinates are in the form x, y,
    where x is a row and y a column and are indexed from 0."""
    empty_fields_set = set()
    for row_index in range(len(board)):
        for column_index in range(len(board[0])):
            if board[row_index][column_index] == '.':
                empty_fields_set.add((row_index, column_index))
    return empty_fields_set


def display_board(board):
    """
    Should print the tic tac toe board in a format similar to
       1   2   3
    A   X | O | .
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | .
       --+---+---
    """
    print("\n")
    print("\t    1     2     3")
    print("\t       |     |")
    print("\tA   {}  |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
    print('\t  _____|_____|_____')
    print("\t       |     |")
    print("\tB   {}  |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
    print('\t  _____|_____|_____')
    print("\t       |     |")
    print("\tC   {}  |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
    print("\t       |     |")
    print("\n")


def is_board_full(board, empty_fields_set_local=False):
    """
    should return True if there are no more empty place on the board,
    otherwise should return False
    """
    if bool(empty_fields_set_local):
        # check if items are tuples of ints
        for item in empty_fields_set_local:
            if isinstance(item, tuple) and len(item) == 2:
                for number in item:
                    if isinstance(number, int) and number < len(board):
                        return False

    list_of_field_states = []
    for i in range(3):
        for j in range(3):
            list_of_field_states.append(board[i][j])
    if "." not in list_of_field_states:
        return True
    else:
        return False


def get_winning_player(board, players):
    """
    Should return the player that wins based on the tic tac toe rules.
    If no player has won, then "None" is returned.
    """
    for player in players:

        if board[0][0] == board[0][1] == board[0][2] == player:
            return player
        elif board[1][0] == board[1][1] == board[1][2] == player:
            return player
        elif board[2][0] == board[2][1] == board[2][2] == player:
            return player
        elif board[0][0] == board[1][0] == board[2][0] == player:
            return player
        elif board[0][1] == board[1][1] == board[2][1] == player:
            return player
        elif board[0][2] == board[1][2] == board[2][2] == player:
            return player
        elif board[0][0] == board[1][1] == board[2][2] == player:
            return player
        elif board[2][0] == board[1][1] == board[0][2] == player:
            return player
    else:
        return None
    # elif board[0][0] == board[0][1] == board[0][2] == "O":
    #     return "O"
    # elif board[1][0] == board[1][1] == board[1][2] == "O":
    #     return "O"
    # elif board[2][0] == board[2][1] == board[2][2] == "O":
    #     return "O"
    # elif board[0][0] == board[1][0] == board[2][0] == "O":
    #     return "O"
    # elif board[0][1] == board[1][1] == board[2][1] == "O":
    #     return "O"
    # elif board[0][2] == board[1][2] == board[2][2] == "O":
    #     return "O"
    # elif board[0][0] == board[1][1] == board[2][2] == "O":
    #     return "O"
    # elif board[2][0] == board[1][1] == board[0][2] == "O":
    #     return "O"


    # import numpy
    # # TODO implement win_line (introduce indexing to the logic below)
    # # win_line is a list representing the winning row, column or diagonal.
    # # Items inside are coordinates represented by a pair of numbers (a tuple) that are coordinates of each field of
    # the winning configuration.
    # # win_line = list()

    # for row in board:
    #     if len(set(row)) == 1 and row[0] != ".":
    #         return row[0]
    # for column in numpy.transpose(board):
    #     if len(set(column)) == 1 and column[0] != ".":
    #         return column[0]
    # if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != ".":
    #     return board[0][0]
    # elif len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1 and board[0][len(board) - 1] != ".":
    #     return board[0][len(board) - 1]
    # else:
    #     return None


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print("Display empty board: ", end='')
    display_board(empty_board)

    board_example = [
        ['X', "O", "."],
        ['X', "O", "."],
        ["O", "X", "."],
    ]
    print("Trying out 'is_board_full()' function on this board:", end='')
    display_board(board_example)
    print("Should return False:")
    print(is_board_full(board_example), "\n")

    board_1 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    display_board(board_1)
    print("Powyżej jest tablica board_1")
    print("--------------------------GET WINNING PLAYER_----------------------------")
    print("WYGRAL: ", get_winning_player(board_1))
    print("Trying out 'is_board_full()' function on this board:", end='')

    print("Should return False:")
    print(is_board_full(board_1), "\n")

    board_2 = [
        [".", "O", "O"],
        [".", "O", "X"],
        [".", "X", "X"],
    ]
    print("Trying out 'is_board_full()' function on this board:", end='')
    display_board(board_2)
    print("Should return False:")
    print(is_board_full(board_2), "\n")

    board_3 = [
        ["O", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "X"],
    ]
    print("Trying out 'is_board_full()' function on this board:", end='')
    display_board(board_3)
    print("Should return True:")
    print(is_board_full(board_3), "\n")

    board_4 = [
        ["X", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("Should return X")
    print(get_winning_player(board_4))

    board_5 = [
        ["X", "O", "O"],
        ["X", "O", "."],
        ["O", "X", "X"],
    ]
    print("Should return O")
    print(get_winning_player(board_5))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("Should return None")
    print(get_winning_player(board_6))
