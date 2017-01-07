from random import randint 

#create empty list
board = []

#add 5 rows of 5 O to list, make a list of lists
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

#use random integer function to define a random row and column wher
#the battleship is hidden
def random_row(board):
    return randint(0, len(board)-1)
    
def random_col(board):
    return randint(0, len(board)-1)
    
#make variables for ship row and colun
ship_row=random_row(board)
ship_col=random_col(board)


#For Debugging print out where the battleship is to make sure
#the correct messages display
#print ship_col
#print ship_row


#use a for loop to set number of tries user has before losing
#for example range(0,4) gives 4 turns
#printing Turn is turn +1 so if turn statement for game over is one less
#than what prints for turn
for turn in range(0,4):
    print "Turn", turn + 1
#use raw input to ask location of guess, row & column
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn ==3:
            print "Game Over"
    
    print_board(board)
