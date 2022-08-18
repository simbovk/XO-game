import tkinter as tk

window = tk.Tk()
window.title("XO Game")

global turn, results
results = ["", "", "", "", "", "", "", "", ""]
turn = "X"

def process(idx):
    global turn
    if results[idx] == "":
        if turn == "X":
            results[idx] = "X"
            buttons[idx]["text"] = "X"
            buttons[idx]["state"] = tk.DISABLED
            turn = "O"
        else:
            results[idx] = "O"
            buttons[idx]["text"] = "O"
            buttons[idx]["state"] = tk.DISABLED
            turn = "X"


def points():
    name_frame = tk.Frame(window)
    name_frame.grid(row=0)
    player_one_label = tk.Label(name_frame, text="player 1", font=("None", 16, "italic"), padx=10)
    player_two_label = tk.Label(name_frame, text="player 2", font=("None", 16, "italic"), padx=10)
    player_one_label.grid(row=0, column=0)
    player_two_label.grid(row=0, column=1)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    player_one_point = tk.Label(point_frame, text="0", font=("None", 16, "italic"), padx=35)
    player_two_point = tk.Label(point_frame, text="0", font=("None", 16, "italic"), padx=50)
    player_one_point.grid(row=0, column=0)
    player_two_point.grid(row=0, column=1)
#
# def rules():



def board():
    global buttons
    buttons = []
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    counter = 0
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame)
            buttons[index].config(width=10, height=4, font=("None", 18, "bold"), command=lambda idx=index: process(idx))
            buttons[index].grid(row=row, column=column)
            counter += 1

points()
board()

window.mainloop()