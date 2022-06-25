from board import display_board, get_empty_board, is_board_full, get_winning_player, get_empty_fields
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates, \
    convert_human_coordinates, perform_move
from menu import get_menu_option, draw_which_player_is_first, AI_NAME, AI_1_NAME, AI_2_NAME
from time import sleep

# from random import seed
# from random import choice

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


#
# def save_record(history_list_local, current_player_local, row_coordinate, column_coordinate):
#     history_list_local.append((current_player_local, row_coordinate, column_coordinate))
#     return history_list_local


def get_coordinates(game_mode, board, current_player):
    # based on the value of the variables `game_mode` and `current_player`
    # the program should choose between the functions
    # get_random_ai_coordinates or get_unbeatable_ai_coordinates or get_human_coordinates

    # x: row of the board coordinate
    # y: column of the boards coordinate
    if game_mode == 1:
        x, y = convert_human_coordinates(get_human_coordinates(board, current_player))
        # save_record(history_list, current_player, x, y)
    elif game_mode == 2:
        x, y = get_random_ai_coordinates(board)
        # save_record(history_list, current_player, x, y)
    elif game_mode == 3:
        if current_player[0] != "random ai":
            x, y = convert_human_coordinates(get_human_coordinates(board, current_player))
            # save_record(history_list, current_player, x, y)
        elif current_player[0] == "random ai":
            x, y = get_random_ai_coordinates(board)
            # save_record(history_list, current_player, x, y)
    elif game_mode == 4:
        if current_player[1] == 'X':
            x, y = convert_human_coordinates(get_human_coordinates(board, current_player))
            # save_record(history_list, current_player, x, y)
        elif current_player[1] == 'O':
            x, y = get_unbeatable_ai_coordinates(board)
    return x, y


def change_player(current_player, player_1, player_2):
    if current_player == player_1:  # current_player must be a tuple (see above player_1/player_2 assignment)
        current_player = player_2
    elif current_player == player_2:
        current_player = player_1
    return current_player


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    # history_list = []

    if game_mode == HUMAN_VS_HUMAN:
        print("Please give names of the players.")
        name_1 = input("Please give the first name:")
        name_2 = input("Please give the second name:")
    elif game_mode == RANDOM_AI_VS_RANDOM_AI:
        name_1 = AI_1_NAME
        name_2 = AI_2_NAME
    elif game_mode == HUMAN_VS_RANDOM_AI:
        name_1 = input("Please enter your name:")
        name_2 = AI_NAME
    elif game_mode == HUMAN_VS_UNBEATABLE_AI:
        name_1 = input("Please enter your name:")
        name_2 = "unbeatable_ai"
    player_1, player_2 = draw_which_player_is_first(name_1, name_2)  # ta funkcja przypisuje do zmiennych
    # player 1, player_2 tuple, która przechowuje imię i symbol ('X' or 'O')
    its_a_tie = False
    # empty_fields = get_empty_fields(board)
    current_player = player_1  # assigning 'O' here makes the 'X' start first.

    is_game_running = True
    while is_game_running:
        display_board(board)

        # in each new iteration of the while loop the program should
        # alternate the value of `current_player` from (name, `X`) to (name, `O`) or from (name, 'O') to (name, 'X') to
        # (name, 'O')


        x, y = get_coordinates(game_mode, board, current_player)
        board = perform_move(board, x, y, current_player[1])
        # save_record(history_list, current_player, x, y)

        # board[x][y] = current_player[1]

        winning_player = get_winning_player(board)
        if winning_player is None and is_board_full(board):
            its_a_tie = True
        if its_a_tie:
            display_board(board)
            print("It is a tie!")
            sleep(4)
        elif winning_player:
            display_board(board)
            try:
                if winning_player == 'X':
                    print(f"{current_player[0]} has won the game!")
                    sleep(4)
                elif winning_player == 'O':
                    print(f"{current_player[0]} has won the game!")
                    sleep(4)
                else:
                    raise ValueError
            except ValueError:
                print("There was an error. Please check if the winning player has been assigned correctly.")

        if its_a_tie or winning_player:
            is_game_running = False

        current_player = change_player(current_player, player_1, player_2)


if __name__ == "__main__":
    main()
