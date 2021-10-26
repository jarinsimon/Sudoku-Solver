board = [
	[1,2,3,4,0,0,0,0,0],
	[0,0,0,1,2,3,4,0,0],
	[4,0,0,0,0,0,1,2,3],
	[0,1,2,3,4,0,0,0,0],
	[0,0,0,0,1,2,3,4,0],
	[3,4,0,0,0,0,0,1,2],
	[0,0,1,2,3,4,0,0,0],
	[0,0,0,0,0,1,2,3,4],
	[2,3,4,0,0,0,0,0,1],
]

#Prints out the current state of the board
def print_board(board):
	#Uses nested for loop to iterate through all spaces on board
	for i in range(len(board)):

		#Draws horizontal lines for grid
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - -")

		for j in range(len(board[0])):
			#Draws vertical lines for grid
			if j % 3 == 0 and j != 0:
				print("| ", end = "")

			#Checks if final column in the grid to not print space
			if j == 8:
				print(board[i][j])		
			#Concatenates number and space 
			else:
				print(str(board[i][j]) + " ", end="")


#Finds empty spaces in board by iterating through all squares
def find_space(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			#Checks if value of current square is 0, which represents an empty space
			if (board[i][j] == 0):
				#Returns position of empty square through coordinates
				return (i, j)
				
	return None


#Algorithm to solve the sudoku board
def solver(board):
	#Check if there are any empty squares on board
	find = find_space(board)

	#If there are no spaces left, exit function because board is solved
	if not find:
		return True

	#Returns row and column coordinates of empty square
	else:
		row, column = find
	
	#Iterate through all rows
	for i in range(1,10):
		if check_valid(board, i, (row, column)):
			board[row][column] = i

			#Recursively calls solve algorithm
			if solver(board):
				return True

			#If recursive call of solver is false, the value of the square is reset to 0
			board[row][column] = 0

	return False

#Checks if number is valid at a specific square
def check_valid(board, number, position):
	#Check if number already exists in the row
	for i in range(len(board[0])):
		if board[position[0]][i] == number and position[1] != i:
			return False
	
	#Check if number already exists in the column 
	for i in range(len(board)):
		if board[i][position[1]] == number and position[0] != i:
			return False

	#Creates boundaries for 3x3 box
	box_x = position[0] // 3
	box_y = position[1] // 3

	#Check if number already exists in box
	for i in range(box_x * 3, box_x * 3 + 3):
		for j in range(box_y * 3, box_y * 3 + 3):
			if board[i][j] == number and (i, j) != position:
				return False
	
	#If number has passed all checks, this is a valid square for the number
	return True


print("\nUnsolved Board\n")
print_board(board)
solver(board)
#print("______________________\n")
print("\nSolved Board\n")
print_board(board)
print("\n")
	