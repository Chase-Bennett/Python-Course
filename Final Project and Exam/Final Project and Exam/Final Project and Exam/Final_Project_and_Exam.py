




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
    human_move = int(input("Enter your move (1-9): "))
    free_fields = make_list_of_free_fields(board)
    move_made = False
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == human_move and (i, j) in free_fields:
                board[i][j] = "O"
                move_made = True
                break
        if move_made:
            break
    if not move_made:
        print("Move not allowed, the field is already taken.")







                
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
 
        # Check rows for victory
        for row in board:
            if all(cell == sign for cell in row):
                return True
        else:
                    return False
        # Check columns for victory
        for col in range(3):
            if all(row[col] == sign for row in board):
                return True
        else:
                    return False
        # Check diagonals for victory
        if all(board[i][i] == sign for i in range(3)):
            return True
        if all(board[i][2 - i] == sign for i in range(3)):
            return True
            
        else:
                    return False
        
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has 
    # won the game)
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):

  try:
        Robot_move=(randrange(8))
        free_fields = make_list_of_free_fields(board)
        move_made = False
  for i, row in enumerate(board):
          for j, col in enumerate(row):
            if col == Robot_move and (i, j) in free_fields:
                board[i][j] = "X"
                move_made = True
                break
            if move_made:
              break
          if not move_made:
           draw_move(board)
  except:print("Tie")
       
        

    # The function draws the computer's move and updates the board.

while victory_for(board, "O") == False and victory_for(board, "X") == False:
    display_board(board)
    enter_move(board)
    draw_move(board)

if victory_for(board, "O") == True:
    print("You win")
if victory_for(board, "X") == True:
    print("You lose")

