def get_human_coordinates(board, current_player):
<<<<<<< HEAD

  letter = ""
  number = 0

  while ((letter != "A" and letter != "B" and letter != "C") or (number != 1 and number != 2 and number != 3)):
    
    letter = input("Enter a line A, B or C: ")
    number = int(input("Enter a column 1, 2 or 3: "))
  
    if ((letter != "A" and letter != "B" and letter != "C") or (number != 1 and number != 2 and number != 3)):
      print("Warning! Invalid input!")
    else:
      print(f"You have chosen {letter}{number} ")
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  pass
=======
    """
    Should return the read coordinates for the tic tac toe board from the terminal.
    The coordinates should be in the format  letter, number where the letter is
    A, B or C and the number 1, 2 or 3.
    If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf)
    then a warning message should appear and the coordinates reading process repeated.
    If the user enters a coordinate that is already taken on the board
    then a warning message should appear and the coordinates reading process repeated.
    If the user enters the word "quit" in any format of capitalised or non-capitalised letters, the program
    should stop.
    """
    pass
>>>>>>> 3368173c61ad8b3f6ed8ca697b6b467a0dc1d9e0


def get_random_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) then "None"
    should be returned.
    """
    pass

def get_unbeatable_ai_coordinates(board, current_player):
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


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    print("It should print the coordinates selected by the human player")
    coordinate_1 = get_human_coordinates(board_1, "X")
    print(coordinate_1)

    board_2 = [
        ["O", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "O"))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "O"))
    print("The printed coordinate should be only (0,2) or (1,2)")
    print(get_random_ai_coordinates(board_2, "O"))

    board_3 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
    ]
    print("The printed coordinate should be None")
    print(get_random_ai_coordinates(board_3))

    board_4 = [
        [".", "O", "."],
        ["X", "O", "."],
        ["X", "X", "O"],
    ]
    print("The printed coordinate should always be (0, 0)")
    print(get_unbeatable_ai_coordinates(board_4, "X"))

    board_5 = [
        ["X", "O", "."],
        ["X", ".", "."],
        ["O", "O", "X"],
    ]
    print("The printed coordinate should always be (1, 1)")
    print(get_unbeatable_ai_coordinates(board_5, "O"))

    board_6 = [
        ["O", "O", "."],
        ["O", "X", "."],
        [".", "X", "."],
    ]
    print("The printed coordinate should either (0, 2) or (2, 0)")
    print(get_unbeatable_ai_coordinates(board_6))
