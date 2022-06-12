from random import choices


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

    chosen_option = int(input('Choose one option from one to four: '))
    while chosen_option < 1 or chosen_option > 4:
        print('Choose one option from one to four: ')
        try:
            chosen_option = int(input())
        except ValueError:
            print("Wrong choice. Please choose option between 1-4")
            # chosen_option = int(input())
            continue
    return chosen_option





if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option)
