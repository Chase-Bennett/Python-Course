




from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def display_board(board):
    print(board)
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    human_move = int(input("Enter your move (1-9): "))
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == human_move:
                board[i][j] = "O"







                
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

"""
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
"""    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):

        Robot_move=(randrange(8))
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                   if col == Robot_move:
                      board[i][j] = "X"

    # The function draws the computer's move and updates the board.




enter_move(board)
print(board)
draw_move(board)
print(board)
