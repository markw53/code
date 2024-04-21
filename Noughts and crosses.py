from random import randint #import library for random numbers
board = ["-","-","-","-","-","-","-","-","-"] #Reset board
game_over=False
turn=0 #For counting number of turns

def print_board(): #Prints the board
  print()
  print(board[0],board[1],board[2])
  print(board[3],board[4],board[5])
  print(board[6],board[7],board[8])
  print()

def which_player(): #Asks player whether they want to be O or X
  while True:
    player_choice = input("Choose X or O, player! > ")
    if player_choice.upper() == "X" or player_choice.upper() == "O":
      return player_choice.upper()
    else:
      print()
      print("Type 'X' or 'O' please")

def player_move(player_char): #Player gives their move
  while True:
    try:
      your_move=input("Your move (type 1 to 9 to choose space to play) > ")
      your_move=int(your_move)
    except ValueError: #error handling for non integers
      print()
      print("Enter a number between 1 and 9.")
      print_board()
      continue
    else:
      if your_move<1 or your_move>9:
        print()
        print("Input number must be between 1 and 9.")
        print_board()
      elif board[your_move-1]=="-":
        board[your_move-1]=player_char
        return board
      else:
        print()
        print("That space is not empty!")
        print_board()
        continue

def check_win(board,character): #Checks to see if board sent to func is in winning position
	if board[0]==character and board[1]==character and board[2]==character:
		return True
	elif board[3]==character and board[4]==character and board[5]==character:
		return True
	elif board[6]==character and board[7]==character and board[8]==character:
		return True
	elif board[0]==character and board[3]==character and board[6]==character:
		return True
	elif board[1]==character and board[4]==character and board[7]==character:
		return True
	elif board[2]==character and board[5]==character and board[8]==character:
		return True
	elif board[0]==character and board[4]==character and board[8]==character:
		return True
	elif board[2]==character and board[4]==character and board[6]==character:
		return True
	else:
		return False

    
		
def computer_move(comp_char,player_char): #Computer decides on move
    
  print("My move!")
  test_board=board #copy the existing board position for calculations

  for space in range(0,9):
    if test_board[space]=="-": #If you can win, win!
      test_board[space]=comp_char
      if check_win(test_board,comp_char)==True:
        board[space]=comp_char
        return board
      else:
        test_board[space]="-"
			
  for space in range(0,9):
    if test_board[space]=="-": #If opponent is threatening to win, block
      test_board[space]=player_char
      if check_win(test_board,player_char)==True:
        board[space]=comp_char
        return board
      else:
        test_board[space]="-"
				
  if test_board[4]=="-": #Favour the centre square if it is free
    board[4]=comp_char
    return board

  for space in range(0,9): #play in first available free space
    if test_board[space]=="-":
      board[space]=comp_char
      return board
	
#Main program

print_board() #Display Board

player_char=which_player() #Select O or X

if player_char == "X": #Assign other character to computer
    comp_char="O"
else:
    comp_char="X"

print("You are playing:",player_char) #Announce who is who
print()
print("The computer plays:",comp_char)
print()
print("Let's play!")
print_board() #Display Board

if randint(0,1)==0: #Randomly assign first player
    next_player="computer"
    print("I go first!")
    print()
else:
    next_player="player"
    print("You go first!")
    print()

#Main game loop below
	
while turn<9 and game_over==False:
    turn+=1 #add 1 to turn
    if next_player=="player": #Player to move
      board=player_move(player_char)
      print_board()
      next_player="computer"
      if check_win(board,player_char)==True:
        print("You win!") #Player wins!
        game_over=True
		
    elif next_player=="computer": #Computer to move
      board=computer_move(comp_char,player_char) #Player character also sent to check for threats
      print_board()
      next_player="player"
      if check_win(board,comp_char)==True:
        print("I win!") #Computer wins!
        game_over=True
			

if game_over==False:
  print("It's a draw!") #No winner

print()
print("Thanks for the game!")