
'''
Solo Checkpoint 02
Author: Bro. Hayes
''' 

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player
    current  = ('x')
    # create a board
    board = create_board()
    
    # loop if there isn't a winner or if the game isn't a draw
    while not (is_winner(board) or is_draw(board)):
        # display the board
        display_board(board)
        # allow the player to make a move
        make_move(current, board)
        # pick the next player
        current = next_player(current)
    # display the final board
    display_board(board)
    # show message for winner and thanks for playing
    print('game over')

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    line = ('-+-+-')
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(line)
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(line)
    print(f'{board[6]}|{board[7]}|{board[8]}')

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    draw = True
    for square in range(9):
        if board[square] != 'x' and board[square] != 'o':
            draw = False

    return draw

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    winner = False
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    square = int(input(f"{player}'s, pick a square (1-9): "))

    while square > 9 or square < 1 or board[square - 1] in ['x', 'o']:
        print('Not a valid space. Choose another.')
        square = int(input(f"{player}'s, pick a square (1-9): "))

    if player == 'x':
        board[square - 1] = 'x'
    else:
        board[square - 1] = 'o'


def next_player(current):
    ''' return: x if current is o, otherwise x '''
    if current == 'x':
        current = 'o'
    else:
        current = 'x'
    return current
# run main if this has been called from the command line
if __name__ == "__main__":
    main()
