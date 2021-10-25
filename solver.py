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

def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - -")
		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print("| ", end = "")

			if j == 8:
				print(board[i][j])		
			else:
				print(str(board[i][j]) + " ", end="")



def find_space(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if (board[i][j]==0):
				return (i, j)
				
	return None



def solver(board):
	find = find_space(board)
	if not find:
		return True
	else:
		row, column = find
	
	for i in range(1,10):
		if check_valid(board, i, (row, column)):
			board[row][column] = i

			if solver(board):
				return True

			board[row][column] = 0

	return False

def check_valid(board, number, position):
	for i in range(len(board[0])):
		if board[position[0]][i] == number and position[1] != i:
			return False
	
	for i in range(len(board)):
		if board[i][position[1]] == number and position[0] != i:
			return False

	box_x = position[1] // 3
	box_y = position[0] // 3

#	print(box_x)
#	print(box_y)

	for i in range(box_y * 3, box_y * 3 + 3):
		for j in range(box_x * 3, box_x*3):
			if board[i][j] == number and (i, j) != position:
				return False
	
	return True




print_board(board)
solver(board)
print("______________________")
print_board(board)
#def solver(board):
	