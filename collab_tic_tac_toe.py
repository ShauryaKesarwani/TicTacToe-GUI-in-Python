import tkinter as tk
from frosch import hook
# ruff: noqa: E501

# Intializing Variables
hook()
plr = "X"
game_won = False

root = tk.Tk()

root.title("Tic Tac Toe")
root.geometry(f'{300}x{320}+{640}+{360}')
root["bg"] = "#ddd6f3"
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.resizable(False, False)

TicTacToeTitle = tk.Label(root, text="Tic Tac Toe", font=("Gotham", 20, "bold"), bg="#ddd6f3")
TicTacToeTitle.grid(row=0, column=0, sticky="ew")

# Check if there is a winner
def check_winner():
    for i in range (len(buttonValues)):
        global game_won
        
        if game_won is True:
            pass
        
        # Horizontal Row Winning Condition
        elif buttonValues[i][0] == buttonValues[i][1] and buttonValues[i][0] == buttonValues[i][2] and buttonValues[i][0] != 0:
            game_won = True
        
        # Vertical Column Winning Condition
        elif buttonValues[0][i] == buttonValues[1][i] and buttonValues[0][i] == buttonValues[2][i] and buttonValues[0][i] != 0:
            game_won = True
        
        # Backward Slanting Winning Condition
        elif buttonValues[i][i] == buttonValues[0][0] and buttonValues[i][i] == buttonValues[1][1] and buttonValues[i][i] == buttonValues[2][2] and buttonValues[i][i] != 0:
            game_won = True
        
        # Forward Slanting Winning Condition
        elif buttonValues[0][2] == buttonValues[1][1] and buttonValues[0][2] == buttonValues[2][0] and buttonValues[0][2] != 0:
            game_won = True
        
    # Tie Condition 
    if check_if_tie() is True:
        reset_game()



    # Winning Code
    if plr == "X" and game_won is True:
        print("Player O won")
        reset_game()
        return True
    elif plr == "O" and game_won is True:
        print("Player X won")
        reset_game()
        return True
    else:
        return False
        
def check_if_tie():
    global game_won
    if game_won is False:
        for i in range(3):
            for j in range(3):
                if buttonValues[i][j] == "X" or buttonValues[i][j] == "O":
                    if i == 2 and j == 2:
                        print("True Tie")
                        return True
                elif buttonValues[i][j] == 0:
                    return False


    else:
        return False


def button_click(row, column):
    global plr
    if plr == "X" and buttonValues[row][column] == 0:
        print(f"Button clicked: Row={row}, Column={column}")
        buttonList[row][column].configure(text = plr, fg="blue")
        buttonValues[row][column] = plr
        plr = "O"

        
    elif plr == "O" and buttonValues[row][column] == 0:
        print(f"Button clicked: Row={row}, Column={column}")
        buttonList[row][column].configure(text = plr, fg="red")
        buttonValues[row][column] = plr
        plr = "X"
        
    check_winner()

def reset_game():
    def onRestartClicked():
        play_area.destroy()
        PlayAreaBuilding()
        RestartBtn.destroy()
        
    RestartBtn = tk.Button(root, text="Restart?", command= onRestartClicked, font=("Gotham", 16, "bold"), bg="#ddd6f3", relief="solid")
    RestartBtn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

def PlayAreaBuilding():
    global game_won, buttonList, buttonValues, plr, play_area
    game_won = False
    plr = "X"
    
    play_area = tk.Frame(root, bg="#ddd6f3")
    play_area.grid(row=1, column=0, sticky="nsew")
    root.bind("<Escape>", lambda e: root.destroy())

    for i in range(3):
        play_area.rowconfigure(i, weight=1)
        play_area.columnconfigure(i, weight=1)

    buttonList = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]

    buttonValues = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]

    for row in range(3):
        for column in range(3):
            buttonList[row][column] = tk.Button(play_area, text=" ", command=lambda r=row, c=column: button_click(r, c), bg="#d4aaff", borderwidth=0, font=("Gotham", 20, "bold"), width=90, height=90)
            buttonList[row][column].grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
            
            def on_enter(button):
                button.widget.config(background='#B591D9')

            def on_leave(button):
                button.widget.config(background='#d4aaff')
            
            buttonList[row][column].bind("<Enter>", lambda button = buttonList[row][column]: on_enter(button))
            buttonList[row][column].bind("<Leave>", lambda button = buttonList[row][column]: on_leave(button))
            
    return

PlayAreaBuilding()

root.mainloop()