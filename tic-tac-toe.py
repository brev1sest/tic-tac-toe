from random import choice

board = [ "1","2","3",
          "4","5","6",
          "7","8","9"]

current_player = "X"

def display_board():
    print(board[0]+" | " +board[1] + " | " + board[2])
    print("-" *2+"|"+"-" *3+"|"+"-" *2)

    print(board[3]+" | " +board[4] + " | " + board[5])
    print("-" *2+"|"+"-" *3+"|"+"-" *2)

    print(board[6]+" | " +board[7] + " | " + board[8])
    print()

def computer_game(player):

    winner = None
    possible_turns = list(range(9))
    display_board()
    
    if player == "O":
        turn = choice(possible_turns)
        board[turn] = "X"
        del possible_turns[possible_turns.index(turn)]
        display_board()
        
    while is_game_over() == False:
        ht  = human_turn(player)
        del possible_turns[possible_turns.index(ht)]
        
        if check_win() == False:
            
            turn = choice(possible_turns)
            board[turn] = flip_player(player)
            del possible_turns[possible_turns.index(turn)]

            display_board()

            if check_win() == True:
                winner = flip_player(player)
        else:
            winner = player
            
    if winner == None and check_tie() == False:
        winner = player

    if winner == "X" or winner ==  "O":
        print()
        print("GAME OVER")
        print(winner + " WON!")
    else:
        print("Tie.")

    
def human_game(current_player):

    display_board()

    while is_game_over() == False:
        handle_turn(current_player)
        current_player = flip_player(current_player)
 
    if check_win():
        winner = flip_player(current_player)
    else:
        winner = None
    if winner == "X" or winner ==  "O":
        print()
        print("GAME OVER")
        print(winner + " WON!")
    else:
        print("Tie.")
    


def handle_turn(current_player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    print(current_player)
    board[position] = current_player
    display_board()

def human_turn(current_player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    print(current_player)
    board[position] = current_player
    display_board()
    return position

    
def flip_player(current_player):
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return current_player

        
def is_game_over():
    return check_win() or check_tie()


def check_lines():
    if board[0] == board[1] == board[2]:
        return True

    elif board[3] == board[4] == board[5]:
        return True    

    elif board[6] == board[7] == board[8]:
        return True

    else:
        return False


def check_columns():
    if board[0] == board[3] == board[6]:
        return True

    elif board[1] == board[4] == board[7]:
        return True    

    elif board[2] == board[5] == board[8]:
        return True

    else:
        return False


def check_diagonals():
    if board[0] == board[4] == board[8]:
        return True

    elif board[3] == board[4] == board[6]:
        return True    

    else:
        return False

      
def check_win():
    
    return check_diagonals() or check_lines() or check_columns()


def check_tie():
    for i in range(9):
        if board[i] == str(i+1):
            return False
    return check_win() == False

    

print("With whom you wanna play? 0 - computer, 1 - human")
opponent = int(input())
if opponent:
    human_game(current_player)
else:
    print("Choose your symbol. O or X")
    player = input()
    computer_game(player) 
