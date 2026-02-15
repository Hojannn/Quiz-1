from tkinter import *
bg_color = "#1B5886"
btn_color = "#3776A1"
win_color = "#467CDF"
tie_color = "#003366"
#switch
def switch(row, column):
    global currentPlayer
    if buttons[row][column]["text"] == "":
        if currentPlayer == "X":
            buttons[row][column]["text"] = currentPlayer
            
            if checkWin() is False:
                currentPlayer = "O"
                label.config(text=(currentPlayer +" turn"))
                
            elif checkWin() is True:
                label.config(text=(currentPlayer+" wins!😃"))
            
            elif checkWin() == "Tie":
                label.config(text=("Tie!😧"))
                
        else: 
            buttons[row][column]["text"] = currentPlayer
            
            if checkWin() is False:
                currentPlayer = "X"
                label.config(text=(currentPlayer+" turn"))
                
            elif checkWin() is True:
                label.config(text=(currentPlayer+" wins!😝"))
            
            elif checkWin() == "Tie":
                label.config(text=("Tie!😧"))
            
#checkWin
def checkWin():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg=win_color)
            buttons[row][1].config(bg=win_color)
            buttons[row][2].config(bg=win_color)
            return True 
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg=win_color)
            buttons[1][column].config(bg=win_color)
            buttons[2][column].config(bg=win_color)
            return True 
    
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            buttons[0][0].config(bg=win_color)
            buttons[1][1].config(bg=win_color)
            buttons[2][2].config(bg=win_color)
            return True 
    
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            buttons[0][2].config(bg=win_color)
            buttons[1][1].config(bg=win_color)
            buttons[2][0].config(bg=win_color)
            return True 
    elif emptySpaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg=tie_color)
        return "Tie"
    else: 
        return False
#checkTie
def emptySpaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
def checkTie():
    pass
#keepPLaying
def keepPlaying():
    global player
    label.config(text=(currentPlayer +" turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=btn_color)


window = Tk()
window.title("Tic Tac Toe")
window.config(bg=bg_color)
currentPlayer = "X"
winner = None
buttons = [[0, 0 , 0,],
           [0, 0, 0], 
           [0, 0, 0]]

label = Label(text= currentPlayer + " turn", font=("consolas", 40), bg=bg_color)
label.pack(side="top")

resetB = Button(text= "reset", font=("consolas", 20), bg=btn_color, command=keepPlaying)
resetB.pack(side="top", padx=10, pady=10)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas,", 40), bg=btn_color,width= 4, height=1, 
                                      command= lambda row= row, column= column: switch(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()
