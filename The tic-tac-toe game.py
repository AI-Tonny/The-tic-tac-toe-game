field = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def selected_figure():
    """
    Prompts the player to select their figure ('X' or 'O') to play with.
    Keeps asking until the player inputs a valid option.
    :return: Returns the chosen figure ('X' or 'O').
    """
    while True:
        selected_shape = input('Choose your figure to play (X - 1 | O - 2): ')
        if selected_shape == '1':
            selected_shape = 'X'
            break
        elif selected_shape == '2':
            selected_shape = 'O'
            break
        else:
            print('Invalid num')

    return selected_shape


def players_turn(selected_item):
    """
    Manages the player's turn by asking for a move (1-9).
    Validates the move to ensure the selected cell is within range and not occupied.
    If the cell is valid, updates the field with the player's symbol ('X' or 'O').
    :param selected_item:
    :return: None return
    """
    while True:
        turn = input(f'Turn {selected_item} | Select a number to move (1 - 9): ')
        if turn.isdigit():
            turn = int(turn)
            if 1 <= turn <= 9:
                row, col = (turn - 1) // 3, (turn - 1) % 3
                if field[row][col] == ' ':
                    field[row][col] = selected_item
                    break
                else:
                    print('Cell is already occupied')
            else:
                print('Turn must be between (1 - 9)')
        else:
            print('Invalid num')


def field_display(field_play):
    """
    Displays the game field in a formatted grid view for the players.
    Separates rows and columns with vertical bars ('|') for better readability.
    :param field_play:
    :return: None return
    """
    for column in field_play:
        i = 0
        for row in range(len(column)):
            if i != len(column) - 1:
                print(column[row], end=' | ')
                i += 1
            else:
                print(column[row])


def check_winning(selected_shape):
    """
    Checks if the current player with the selected figure ('X' or 'O') has won.
    Evaluates rows, columns, and diagonals for three matching symbols in a row.
    :param selected_shape:
    :return: Returns True if a win is detected; otherwise, returns False.
    """
    for row in field:
        if row.count(selected_shape) == 3:
            return True

    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] == selected_shape:
            return True

    if field[0][0] == field[1][1] == field[2][2] == selected_shape:
        return True
    if field[0][2] == field[1][1] == field[2][0] == selected_shape:
        return True

    return False


def main():
    """
    The main game loop. Initializes the game, starting with player input for figure selection.
    Alternates turns between players, checking for a win or a draw after each move.
    Ends the game when a player wins or all cells are filled (draw).
    :return: None return
    """
    input('Press enter to start game!')
    print('-------------------------------')
    selected_shape = selected_figure()
    while True:
        players_turn(selected_shape)
        field_display(field)
        winning = check_winning(selected_shape)
        if winning:
            print(f'Player {selected_shape} | WIN this game!')
            break
        elif all(cell != ' ' for row in field for cell in row):
            print('Draw\'s moves are over.')
            break

        if selected_shape == 'X':
            selected_shape = 'O'
        elif selected_shape == 'O':
            selected_shape = 'X'


if __name__ == '__main__':
    main()
