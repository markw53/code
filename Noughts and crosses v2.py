def display_board(board):
    print(board[7]+"¦"+board[8]+"¦"+board[9])
    print("-¦-¦-")
    print(board[4]+"¦"+board[5]+"¦"+board[6])
    print("-¦-¦-")
    print(board[1]+"¦"+board[2]+"¦"+board[3])
    print("-¦-¦-")
testing_board=[" "]*10
display_board(testing_board)

def player_input():
    marker=" "
    while marker !="x" or marker !="o":
        marker = input("player 1 choose x,o: ")

        if marker=="o":
            return("o","x")
        elif marker=="x":
            return("x","o")
        else:
            return("Please choose appropriate marker")
player_input()
    
import random

def first_move():
    if random.randint(0,1)==0:
        return "player 2 will start the game"
    else:
        return "player 1 will start the game"

def handle_turn(board,marker,position):
    board[position]=marker
handle_turn(testing_board,"x",5)
display_board(testing_board)

def space_free(board,position):
    return board[position]==" "
space_free(testing_board,5)

def fullboardcheck(board):
    for i in range(1,10):
        if space_free(board,i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_free(board,position):
        position = int(input("Choose your next position: (1-9)"))
    return position

def check_win(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or (board[1]==mark and board[2]==mark and board[3]==mark) or (board[7]==mark and board[4]==mark and board[1]==mark) or (board[8]==mark and board[5]==mark and board[2]==mark) or (board[9]==mark and board[6]==mark and board[3]==mark) or (board[7]==mark and board[5]==mark and board[3]==mark) or (board[9]==mark and board[5]==mark and board[1]==mark))

def replay():
    return input("Do you want to play again? Enter Yes or No: ")

while True:
    theBoard=[' '] *10
    player1_marker,player2_marker = player_input()
    turn = first_move()
    print(turn + " and will go first")

    #game play
    play_game = input("Are you ready to play? Enter Yes or No.")

if play_game == ("Yes"):
    game_is_on = True
else:
    game_is_on = False

while game_is_on:
    if turn == "player 1":
        display_board(theBoard)
        print("player 1")
        position=player_choice(theBoard)
        handle_turn(theBoard,player1_marker,position)

        if check_win(theBoard,player1_marker):
            display_board(theBoard)
            print("Congratulations! player 1 has won the game!")
            game_is_on=False
        else:
            if fullboardcheck(theBoard):
                display_board(theBoard)
                print("The game is a draw!")
                break
            else:
                turn = "player 2"

    else:
        display_board(theBoard)
        print("player 2")
        position = player_choice(theBoard)
        handle_turn(theBoard, player2_marker, position)

        if check_win(theBoard, player2_marker):
            display_board(theBoard)
            print("Player 2 has won the game!")
            game_is_on = False

        else:
            if fullboardcheck(theBoard):
                display_board(theBoard)
                print("The game is a draw!")
                break
            else:
                 turn = "player 1"

        if not replay():
            break
