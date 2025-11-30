def print_board(board):

  print("\n")

  print(board[0] + " | " + board[1] + " | " + board[2])

  print("--+---+--")

  print(board[3] + " | " + board[4] + " | " + board[5])

  print("--+---+--")

  print(board[6] + " | " + board[7] + " | " + board[8])

  print("\n")
 
def check_win(board, player):
    win_conditions=[[0,1,2], [3,4,5],[6,7,8],[0,3,6], [1,4,7], [2,5,8],[0,4,8], [2,4,6]]
    for condition in win_conditions:
     if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
       return True
    return False
def check_draw(board) :
    return " " not in board
def player_move(board, player):
    while True:
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if pos >= 0 and pos < 9 and board[pos] == " ":
         board[pos] = player
         break
        else:  
            print ("Invalid choice")
def tic_tac_toe():
 board = [" "] * 9
 current_player = "x"
 while True:
  print_board(board)
  player_move(board, current_player)
  if check_win(board, current_player):
   print_board(board)
   print(f"Player {current_player} wins!")
   break

 if check_draw (board):
    print_(board)
    print ("It's a draw!")
 current_player= "o" if current_player == "x" else "x"

tic_tac_toe()