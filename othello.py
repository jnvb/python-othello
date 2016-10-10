import Tkinter

top = Tkinter.Tk()
top.title("Othello")

score = [2, 2]
score_label = Tkinter.Button(text="black turn!")
score_label.grid(row=0, column=0)
bla = Tkinter.Button(text="black")
bla.grid(row=0, column=1)
black = Tkinter.Button(text=str(score[0]))
black.grid(row=0, column=2)
bla = Tkinter.Button(text=":")
bla.grid(row=0, column=3)
white = Tkinter.Button(text=str(score[1]))
white.grid(row=0, column=4)
bla = Tkinter.Button(text="white")
bla.grid(row=0, column=5)

size = 8
a = size/2
b = size/2-1

# 1 = white, 0 = black
board = [[9 for i in range(0, size+2)] for k in range(0,size+2)]
board[b][b] = 1
board[b][a] = 0
board[a][b] = 0
board[a][a] = 1

def show():
	for i in range(0, size):
		for k in range(0, size):
			print board[i][k],
		print ""

r = -1
c = 0
color = "grey"
list_box = {}
list_coord = {}
turn = 0
player_color = ["black", "white"]

def callback(event):
	tmp = ""
	box = event.widget
	try:
		tmp = list_box[box].split("|")
	except:
		return None

	global turn, score

	b = 0
	player = turn % 2
	r = int(tmp[0])
	c = int(tmp[1])

	"""
	+-------+-------+-------+
	|       |       |       |
	| -1,-1 | 0, -1 | 1, -1 | 
	|       |       |       |
	+-------+-------+-------+
	|       |       |       |
	| -1, 0 |       | 1 , 0 | 
	|       |       |       |
	+-------+-------+-------+
	|       |       |       |
	| -1, 1 | 0 , 1 | 1 , 1 | 
	|       |       |       |
	+-------+-------+-------+
	"""

	if board[r][c] == 9:
		#--->
		if board[r][c+1] == (player+1)%2 and board[r][c+2] != 9:
			for i in range(c+1, size):
				if board[r][i] == player:
					for k in range(c+1, i):
						list_coord[str(r)+"|"+str(k)].configure(background=player_color[player])
						board[r][k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#<---
		if board[r][c-1] == (player+1)%2 and board[r][c-2] != 9:
			for i in range(c-1, -1, -1):
				if board[r][i] == player:
					for k in range(c-1, i, -1):
						list_coord[str(r)+"|"+str(k)].configure(background=player_color[player])
						board[r][k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#downside
		if board[r+1][c] == (player+1)%2 and board[r+2][c] != 9:
			for i in range(r+1, size):
				if board[i][c] == player:
					for k in range(r+1, i):
						list_coord[str(k)+"|"+str(c)].configure(background=player_color[player])
						board[k][c] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#upside
		if board[r-1][c] == (player+1)%2 and board[r-2][c] != 9:
			for i in range(r-1, -1, -1):
				if board[i][c] == player:
					for k in range(r-1, i, -1):
						list_coord[str(k)+"|"+str(c)].configure(background=player_color[player])
						board[k][c] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#diag right, down
		if board[r+1][c+1] == (player+1)%2 and board[r+2][c+2] != 9:
			tmp = 0
			if size-c <= r:
				tmp = r
			else:
				tmp = size-c
			for i in range(1, tmp):
				if board[r+i][c+i] == player:
					for k in range(1, i):
						list_coord[str(r+k)+"|"+str(c+k)].configure(background=player_color[player])
						board[r+k][c+k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#diag left,up
		if board[r-1][c-1] == (player+1)%2 and board[r-2][c-2] != 9:
			tmp = 0
			if c <= r:
				tmp = c
			else:
				tmp = r
			for i in range(1, tmp+1):
				if board[r-i][c-i] == player:
					for k in range(1, i):
						list_coord[str(r-k)+"|"+str(c-k)].configure(background=player_color[player])
						board[r-k][c-k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#diag right, down
		if board[r-1][c+1] == (player+1)%2 and board[r-2][c+2] != 9:
			tmp = 0
			if size-c <= r:
				tmp = size-c
			else:
				tmp = r
			for i in range(1, tmp):
				if board[r-i][c+i] == player:
					for k in range(1, i):
						list_coord[str(r-k)+"|"+str(c+k)].configure(background=player_color[player])
						board[r-k][c+k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		#diag left, down
		if board[r+1][c-1] == (player+1)%2 and board[r+2][c-2] != 9:
			tmp = 0
			if size-c-1 < r:
				tmp = c
			else:
				tmp = size-r
			for i in range(1, tmp):
				if board[r+i][c-i] == player:
					for k in range(1, i):
						list_coord[str(r+k)+"|"+str(c-k)].configure(background=player_color[player])
						board[r+k][c-k] = player
						score[player] += 1
						score[(player+1)%2] -= 1
					b = 1
					break

		if b:
			score[player] += 1
			score_label.configure(text=player_color[(player+1)%2]+" turn!")
			black.configure(text=str(score[0]))
			white.configure(text=str(score[1]))
			board[r][c] = player
			box.configure(background=player_color[player])
			turn += 1

top.bind("<Button-1>", callback)

# initialize the gameboard
for i in range(0, pow(size, 2)):
	if i % size == 0:
		r += 1
		c = 0
	else:
		c += 1

	if board[r][c] == 1:
		color = "white"
	elif board[r][c] == 0:
		color = "black"
	else:
		color = "#498658"

	a = Tkinter.Canvas(width=100, height=100, background=color, highlightbackground="#1E2426")
	list_box[a] = str(r)+"|"+str(c)
	list_coord[str(r)+"|"+str(c)] = a
	a.grid(row=r+1, column=c)

top.mainloop()