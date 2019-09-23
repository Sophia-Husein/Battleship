from random import randint
board = []
turn = 0
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def guessing():
	global turn 
	turn = turn + 1
	guess_row = int(input("Guess Row: ")) - 1
	guess_col = int(input("Guess Col: ")) - 1
	

	if guess_row == ship_row and guess_col == ship_col:
	    print ("Congratulations! You sunk my battleship!")
	elif turn == 4:
		print ("Game Over")
	else:
	    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
	        print ("Oops, that's not even in the ocean.")
	        guessing()
	    elif(board[guess_row][guess_col] == "X"):
	        print ("You guessed that one already.")
	        guessing()
	    else:
	        print ("You missed my battleship!")
	        board[guess_row][guess_col] = "X"
	        print_board(board)
	        guessing()

print ("Let's play Battleship!")
print_board(board)
ship_row = int(random_row(board))
ship_col = int(random_col(board))

guessing()
