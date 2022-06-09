def get_empty_board():
  board_0 = [
  [".", ".", "."], 
  [".", ".", "."], 
  [".", ".", "."],
  ]
  return board_0
  '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    
    '''  


def display_board(board):
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


def is_board_full(board):
  list=[]
  for i in range(3):
    for j in range(3):
      list.append(board[i][j])
  if "." not in list:
    return True 
  else:
    return False
  """
  should return True if there are no more empty place on the board,
  otherwise should return False
  """


def get_winning_player(board):
  if board[0][0] == board[0][1] == board[0][2] == "X":
    return ("Player X has won")
  elif board[1][0] == board[1][1] == board[1][2] == "X":
    return ("Player X has won")
  elif board[2][0] == board[2][1] == board[2][2] == "X":
    return ("Player X has won")
  elif board[0][0] == board[1][0] == board[2][0] == "X":
    return ("Player X has won")
  elif board[0][1] == board[1][1] == board[2][1] == "X":
    return ("Player X has won")
  elif board[0][2] == board[1][2] == board[2][2] == "X":
    return ("Player X has won")
  elif board[0][0] == board[1][1] == board[2][2] == "X":
    return ("Player X has won")
  elif board[2][0] == board[1][1] == board[0][2] == "X":
    return ("Player X has won")
  elif board[0][0] == board[0][1] == board[0][2] == "O":
    return ("Player O has won")
  elif board[1][0] == board[1][1] == board[1][2] == "O":
    return ("Player O has won")
  elif board[2][0] == board[2][1] == board[2][2] == "O":
    return ("Player O has won")
  elif board[0][0] == board[1][0] == board[2][0] == "O":
    return ("Player O has won")
  elif board[0][1] == board[1][1] == board[2][1] == "O":
    return ("Player O has won")
  elif board[0][2] == board[1][2] == board[2][2] == "O":
    return ("Player O has won")
  elif board[0][0] == board[1][1] == board[2][2] == "O":
    return ("Player O has won")
  elif board[2][0] == board[1][1] == board[0][2] == "O":
    return ("Player O has won")
  else:
    return ("None")

  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  pass


# run this file to test whether you have correctly implemented the functions
if __name__ == "__main__":
    empty_board = get_empty_board()
    print(empty_board)

    board_example = [
      ['X', "O", "."],
      ['X', "O", "."],
      ["O", "X", "."],
    ]
    print("""
    should print 
        1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       ---+---+---
    C   O | X | . 
       ---+---+---
    """)
    
    display_board(board_example)
    
    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print("Should return False")
    print(is_board_full(board_1)) 

    board_2 = [
      [".", "O", "O"],
      [".", "O", "X"],
      [".", "X", "X"],
    ]
    print("Should return False")
    print(is_board_full(board_2)) 

    board_3 = [
      ["O", "O", "X"],
      ["O", "X", "O"],
      ["O", "X", "X"],
    ]
    print("Should return True")
    print(is_board_full(board_3)) 

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