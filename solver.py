# *********************
#    SUDOKU SOLVER 
# *********************


import numpy as np


# Read The Board
data_entry = np.loadtxt("test.txt",skiprows=2)
# Debugging step
d = np.asarray(data_entry, dtype=int)
board = d

# Some Basic Visualization

print(" ------------------------------- ")
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[0][0],d[0][1],d[0][2],d[0][3],d[0][4],d[0][5],d[0][6],d[0][7],d[0][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[1][0],d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6],d[1][7],d[1][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[2][0],d[2][1],d[2][2],d[2][3],d[2][4],d[2][5],d[2][6],d[2][7],d[2][8]))
print(" ------------------------------- ")
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[3][0],d[3][1],d[3][2],d[3][3],d[3][4],d[3][5],d[3][6],d[3][7],d[3][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[4][0],d[4][1],d[4][2],d[4][3],d[4][4],d[4][5],d[4][6],d[4][7],d[4][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[5][0],d[5][1],d[5][2],d[5][3],d[5][4],d[5][5],d[5][6],d[5][7],d[5][8]))
print(" ------------------------------- ")
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[6][0],d[6][1],d[6][2],d[6][3],d[6][4],d[6][5],d[6][6],d[6][7],d[6][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[7][0],d[7][1],d[7][2],d[7][3],d[7][4],d[7][5],d[7][6],d[7][7],d[7][8]))
print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[8][0],d[8][1],d[8][2],d[8][3],d[8][4],d[8][5],d[8][6],d[8][7],d[8][8]))
print(" ------------------------------- ")


# -----------------------------------------------
# Function : Check if the move is valid or not
# -----------------------------------------------

# input : Row and Column number where value is 0
# returns : good move (TRUE) or bad move (FALSE)
# -----  validity = 0 (bad move)   ----- 
# -----  validity = 1 (good move)  -----


def valid_move(board,row,col,number):
	validity = 1
	
	# check whether the number is seen in the row below or side columns
	for i in range(0,9):
		if board[row][i] == number:
			validity = 0
		
	for i in range(0,9):
		if board[i][col] == number:
			validity = 0

	row = row - row%3
	col = col - col%3

	# check if the number is repeating in the 3x3 grid
	for i in range(0,3):
		for j in range(0,3):
			if board[row+i][col+j] == number:
				validity = 0


	if validity == 0:
		return False
	else:
		return True


# ------------------------------------------------
# Function : Sudoku Solver based on BackTracking
# ------------------------------------------------

# ----- game : 0 | The Game is ON.     -----
# ----- game : 1 | The Game is Solved. -----

def sudoku_solver(board):

	game = 1
	
	# find empty spaces // in our case, where there is zero
	for x in range(0,9):
		for xx in range(0,9):
			if board[x][xx] == 0:
				row_empty = x
				col_empty = xx
				game = 0
				break
	
	if game==1:
		
		# ----------------
		# FINAL BOARD
		# ----------------

		d = board

		print("\n ---------  BACKTRACKING ALGORITHM SOLUTION  --------- \n")
		
		print(" ------------------------------- ")
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[0][0],d[0][1],d[0][2],d[0][3],d[0][4],d[0][5],d[0][6],d[0][7],d[0][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[1][0],d[1][1],d[1][2],d[1][3],d[1][4],d[1][5],d[1][6],d[1][7],d[1][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[2][0],d[2][1],d[2][2],d[2][3],d[2][4],d[2][5],d[2][6],d[2][7],d[2][8]))
		print(" ------------------------------- ")
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[3][0],d[3][1],d[3][2],d[3][3],d[3][4],d[3][5],d[3][6],d[3][7],d[3][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[4][0],d[4][1],d[4][2],d[4][3],d[4][4],d[4][5],d[4][6],d[4][7],d[4][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[5][0],d[5][1],d[5][2],d[5][3],d[5][4],d[5][5],d[5][6],d[5][7],d[5][8]))
		print(" ------------------------------- ")
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[6][0],d[6][1],d[6][2],d[6][3],d[6][4],d[6][5],d[6][6],d[6][7],d[6][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[7][0],d[7][1],d[7][2],d[7][3],d[7][4],d[7][5],d[7][6],d[7][7],d[7][8]))
		print(" | {}  {}  {} | {}  {}  {} | {}  {}  {} | ".format(d[8][0],d[8][1],d[8][2],d[8][3],d[8][4],d[8][5],d[8][6],d[8][7],d[8][8]))
		print(" ------------------------------- \n")

		exit(0)

	# row and col shows where are the zeros.
	# Now, all we want to do is play the game by making a guess.

	for guess in range(1,10):
		if valid_move(board, row_empty, col_empty, guess):
			board[row_empty][col_empty] = guess
		
			if sudoku_solver(board):
				return True
			
			board[row_empty][col_empty]=0

	return False

sudoku_solver(board)
