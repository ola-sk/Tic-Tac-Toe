from random import choice


def draw_which_player_is_first(name_1, name_2):
    # wylosuj kolejność
    player_1 = choice([name_1, name_2])
    player_2 = None
    if player_1 == name_1:
        player_2 = name_2
    elif player_1 == name_2:
        player_2 = name_1

    if player_1 != "random ai" and player_1 != "random_ai_1" and player_1 != "random_ai_2":
        symbol_1 = input(player_1 + " please choose 'X' or 'O': ")
    # wprowadź weryfikację danych użytkownika
        symbol_2 = None
    elif player_1 == "random ai" or player_1 =="random_ai_1" or player_1 =="random_ai_2":
        symbol_1 = choice(['X','O'])
        symbol_2 = None

    if symbol_1 == 'X':
        symbol_2 = 'O'
    elif symbol_1 == 'O':
        symbol_2 = 'X'
    print(player_1, "is", symbol_1, "and", player_2, "is", symbol_2)
    return (player_1, symbol_1), (player_2, symbol_2)


def get_menu_option():
    """
    Should print a menu with the following options:
    1. Human vs Human
    2. Random AI vs Random AI
    3. Human vs Random AI
    4. Human vs Unbeatable AI

    The function should return a number between 1-4.
    If the user will enter invalid data (for example 5), than a message will appear
    asking to input a new value.
    """

    print("""
        1. Human vs Human
        2. Random AI vs Random AI
        3. Human vs Random AI
        4. Human vs Unbeatable AI
        """)
    print("Choose one option from one to four: ")
    while True:
        try:
            chosen_option = int(input())
        except ValueError:
            print("Please enter a number! Choose from 1-4: ")
            continue
        if chosen_option < 1 or chosen_option > 4:
            print("Wrong choice. Please choose option between 1-4")
            continue
        else:
            return chosen_option





if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)
