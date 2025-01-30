

"""


from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def display_board(board):
  print("----------")
  print(board[0][0], "|", board[0][1], "|", board[0][2])
  print(board[1][0], "|", board[1][1], "|", board[1][2])
  print(board[2][0], "|", board[2][1], "|", board[2][2])
  print("----------")
                          
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    free_fields = make_list_of_free_fields(board)

    if not free_fields:  # Prevents unnecessary input when board is full
        return

    while True:
        try:
            human_move = int(input("Enter your move (1-9): "))

            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == human_move:
                        board[i][j] = "O"
                        return  # Exit function after successful move

            print("Move not allowed, the field is already taken.")
        except ValueError:
            print("Invalid input! Please enter a number between 1-9.")








                
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):

        free_fields = []
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != "X" and col != "O":
                    free_fields.append((i, j))
        return free_fields
   
                
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

            


 
def victory_for(board, sign):
    # Check rows
    for row in board:
        if all(cell == sign for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False  # If no win condition is met

        
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has 
    # won the game)
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):

    from random import randrange
    free_fields = make_list_of_free_fields(board)
    
    if not free_fields:  # Check if there are any moves left
       print("Tie")
       return
    
    i, j = free_fields[randrange(len(free_fields))]  # Pick a random free spot
    board[i][j] = "X"

        
  
       
        

    # The function draws the computer's move and updates the board.

while not victory_for(board, "O") and not victory_for(board, "X"):
    display_board(board)

    # Get human move
    enter_move(board)

    # Check if human won
    if victory_for(board, "O"):
        display_board(board)
        print("You win!")
        break

    # Check if the board is full before letting the computer move
    if not make_list_of_free_fields(board):
        print("Tie!")
        break

    # Computer makes a move
    draw_move(board)

    # Check if computer won
    if victory_for(board, "X"):
        display_board(board)
        print("You lose!")
        break

# Final board display after the game ends
display_board(board)


"""
