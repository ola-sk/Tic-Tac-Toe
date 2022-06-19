from board import display_board, get_empty_board, is_board_full, get_winning_player, get_empty_fields
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates, \
    convert_human_coordinates, perform_move
from menu import get_menu_option, draw_which_player_is_first
from random import seed
from random import choice

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def save_record(history_list_local, current_player_local, row_coordinate, column_coordinate):
    history_list_local.append((current_player_local, row_coordinate, column_coordinate))
    return history_list_local


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    history_list = []
    if game_mode == 1:
        print("Please give names of the players.")
        name_1 = input("Please give the first name:")
        name_2 = input("Please give the second name:")
        player_1, player_2 = draw_which_player_is_first(name_1, name_2)  # ta funkcja przypisuje do zmiennych
        # player 1, player_2 tuple, która przechowuje imię i symbol ('X' or 'O')
        # print(player_1[0], "please choose the coordinate: ")
        # print("Player_1: ", player_1)
        # print("Player_2: ", player_2)
    if game_mode == 2:
        name_1 = input("Please enter your name:")
        name_2 = "random ai"
        player_1, player_2 = draw_which_player_is_first(name_1, name_2)
    its_a_tie = False
    # empty_fields = get_empty_fields(board)
    try:
        current_player = player_2  # assigning 'O' here makes the 'X' start first.
        if current_player != player_2 and current_player != player_1:
            raise ValueError
    except ValueError:
        print("Please set the current player to have the symbol in the game set as either 'O' or 'X'. Currently "
              "the game doesn't work with characters others than those.")
        # TODO make a proper exception handling: create a function that will get another proper value assigned to the
        #  current_player
    is_game_running = True
    while is_game_running:
        display_board(board)

        # TODO ###
        # in each new iteration of the while loop the program should
        # alternate the value of `current_player` from `X` to `O`
        try:
            if current_player == player_1:
                current_player = player_2
            elif current_player == player_2:
                current_player = player_1
            else:
                raise ValueError
        except ValueError:
            print("Something went wrong! Please set the current player to have the symbol in the game set as "
                  "either 'O' or 'X'. Currently the game doesn't work with characters others than those.")
            # TODO make a proper exception handling: create a function that will get another proper value assigned to
            #  the current_player


        # TODO ###
        # Ustalić kto zaczyna pierwszy. Być może zrobić opcję wyboru znaku przez gracza na początku rozgrywki lub human
        # player zawsze zaczyna pierwszy krzyżykiem.

        # based on the value of the variables `game_mode` and `current_player`
        # the program should choose between the functions
        # get_random_ai_coordinates or get_unbeatable_ai_coordinates or get_human_coordinates

        # x: row of the board coordinate
        # y: column of the boards coordinate
        if game_mode == 1:
            x, y = convert_human_coordinates(get_human_coordinates(board, current_player))
            board = perform_move(board, x, y, current_player[1])
            save_record(history_list, current_player, x, y)
        elif game_mode == 2:
            x, y = get_random_ai_coordinates(board)
            board = perform_move(board, x, y, current_player[1])
            save_record(history_list, current_player, x, y)
        elif game_mode == 3:
            if current_player == 'X':
                x, y = convert_human_coordinates(get_human_coordinates(board))
                board = perform_move(board, x, y, current_player[1])
                save_record(history_list, current_player, x, y)
            elif current_player == 'O':
                x, y = get_random_ai_coordinates(board)
                board = perform_move(board, x, y, current_player[1])
                save_record(history_list, current_player, x, y)
        elif game_mode == 4:
            if current_player == 'X':
                x, y = convert_human_coordinates(get_human_coordinates(board))
                board = perform_move(board, x, y, current_player[1])
                save_record(history_list, current_player, x, y)
            elif current_player == 'O':
                x, y = get_unbeatable_ai_coordinates(board)
                board = perform_move(board, x, y, current_player[1])
                save_record(history_list, current_player, x, y)

        board[x][y] = current_player[1]

        # TODO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        if winning_player is None and is_board_full(board):
            its_a_tie = True
        if its_a_tie:
            print("It is a tie!")
        elif winning_player:
            try:
                if winning_player == 'X':
                    print("X has won the game!")
                elif winning_player == 'O':
                    print("O has won the game!")
                else:
                    raise ValueError
            except ValueError:
                print("There was an error. Please check if the winning player has been assigned correctly.")

        if its_a_tie or winning_player:
            is_game_running = False


if __name__ == "__main__":
    main()
