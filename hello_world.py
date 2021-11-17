board = [' ' for x in range(10)]

def print_board(board):
    print("  |    |")
    print(board[1] + " | " + board[2], " | ", board[3])
    print("-----------")
    print("  |    |")
    print(board[4] + " | " + board[5], " | ", board[6])
    print("-----------")
    print("  |    |")
    print(board[7] + " | " + board[8], " | ", board[9])

    

def is_winner(board, let):
    return board[1] == let and board[2] == let and board[3] == let or \
           board[4] == let and board[5] == let and board[6] == let or \
           board[7] == let and board[8] == let and board[9] == let or \
           board[1] == let and board[4] == let and board[7] == let or \
           board[2] == let and board[5] == let and board[8] == let or \
           board[3] == let and board[6] == let and board[9] == let or \
           board[1] == let and board[5] == let and board[9] == let or \
           board[3] == let and board[5] == let and board[7] == let           

def insert_let(let, pos):
    board[pos] = let


def is_board_full(board):
    if board.count(" ") < 1:
        return True
    else:
        return False 

def space_is_free(pos):
    if board[pos] == " ":
        return True 
    else:
        return False


def player_one_move():
    run = True
    while run:
        move = input("insert the postion number to place your 'X' : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_let("X", move)
                else:
                    print("space is already taken")
            else:
                print("please insert a numner in range of (1-9)")

        except:
            print("please insert a number value only ")


def player_two_move():
    run = True
    while run:
        move = input("insert the postion number to place your 'O' : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_let("O", move)
                else:
                    print("space is already taken")
            else:
                print("please insert a numner in range of (1-9)")

        except:
            print("please insert a number value only ")


def main_game():

    print("welcome to tic tac toe")
    player_one = input("please put name for player one who will be playing as (X): ")
    player_two = input("please put name for player two who will be playing as (O): ")
    print_board(board)
    while not is_board_full(board):
        if not (is_winner(board, "O")):
            player_one_move()
            print_board(board)
        else:
            print(f" {player_two} have won the game")
            break

        if not (is_winner(board, "X")):
            player_two_move()
            print_board(board)
        else:
            print(f" {player_one} have won the game ")
            break
    if is_board_full(board):
        print("Tie Game")



main_game()
