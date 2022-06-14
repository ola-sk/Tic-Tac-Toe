from board import display_board, get_empty_board, is_board_full, get_winning_player, get_empty_fields
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates, \
    convert_human_coordinates, perform_move
from menu import get_menu_option

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def save_record(history_list_local, current_player_local, row_coordinate, column_coordinate):
    history_list_local.append(current_player_local, row_coordinate, column_coordinate)
    return history_list_local


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    history_list = []
    empty_fields = get_empty_fields(board)
    try:
        current_player = 'O' # assigning 'O' here makes the 'X' start first.
        if current_player != 'O' or current_player != 'X':
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
            if current_player == 'X':
                current_player = 'O'
            elif current_player == 'O':
                current_player = 'X'
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
            x, y = convert_human_coordinates(get_human_coordinates(board))
            board = perform_move(board, x, y, current_player)
            save_record(history_list, current_player, x, y)
        elif game_mode == 2:
            x, y = get_random_ai_coordinates(board)
            board = perform_move(board, x, y, current_player)
            save_record(history_list, current_player, x, y)
        elif game_mode == 3:
            if current_player == 'X':
                x, y = convert_human_coordinates(get_human_coordinates(board))
                board = perform_move(board, x, y, current_player)
                save_record(history_list, current_player, x, y)
            elif current_player == 'O':
                x, y = get_random_ai_coordinates(board)
                board = perform_move(board, x, y, current_player)
                save_record(history_list, current_player, x, y)
        elif game_mode == 4:
            if current_player == 'X':
                x, y = convert_human_coordinates(get_human_coordinates(board))
                board = perform_move(board, x, y, current_player)
                save_record(history_list, current_player, x, y)
            elif current_player == 'O':
                x, y = get_unbeatable_ai_coordinates(board)
                board = perform_move(board, x, y, current_player)
                save_record(history_list, current_player, x, y)

        board[x][y] = current_player

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
