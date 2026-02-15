
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPLayer =  "X"
winner = None
gameRunning = True

#printBoard
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#playerInput
def playerinp(board):
    inp = int(input("Choose a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPLayer
    else:
        print("Spot's taken... Try again.")
        
#checkWinorTie
def column(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print_board(board)
        print("It's a Tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if column(board) or row(board) or diag(board):
        print_board(board)
        print(f"The winner is {winner}!")
        gameRunning = False
        
#switch
def switch():
    global currentPLayer
    if currentPLayer == "X":
        currentPLayer = "O"
    else:
        currentPLayer = "X"

#keepPlaying
while gameRunning:
    print_board(board)
    playerinp(board)
    switch()
    checkWin()
    checkTie(board)