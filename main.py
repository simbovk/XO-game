import tkinter as tk
from tkinter.messagebox import showinfo


window = tk.Tk()
window.title("XO Game")

global turn, results, player_points
results = ["", "", "", "", "", "", "", "", ""]
turn = "X"
player_points = [0, 0]

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
        rules()

def points():
    name_frame = tk.Frame(window)
    name_frame.grid(row=0)
    player_one_label = tk.Label(name_frame, text="player 1", font=("None", 16, "italic"), padx=10)
    player_two_label = tk.Label(name_frame, text="player 2", font=("None", 16, "italic"), padx=10)
    player_one_label.grid(row=0, column=0)
    player_two_label.grid(row=0, column=1)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    player_one_point = tk.Label(point_frame, text=player_points[0], font=("None", 16, "italic"), padx=35)
    player_two_point = tk.Label(point_frame, text=player_points[1], font=("None", 16, "italic"), padx=50)
    player_one_point.grid(row=0, column=0)
    player_two_point.grid(row=0, column=1)

def rules():
    if results[0] == results[1] == results[2] and results[0] != "":
        show_winner(results[0])
    if results[3] == results[4] == results[5] and results[3] != "":
        show_winner(results[3])
    if results[6] == results[7] == results[8] and results[6] != "":
        show_winner(results[6])
    if results[0] == results[3] == results[6] and results[0] != "":
        show_winner(results[0])
    if results[1] == results[4] == results[7] and results[1] != "":
        show_winner(results[1])
    if results[2] == results[5] == results[8] and results[2] != "":
        show_winner(results[2])
    if results[0] == results[4] == results[8] and results[0] != "":
        show_winner(results[0])
    if results[2] == results[4] == results[6] and results[2] != "":
        show_winner(results[2])

def show_winner(winner):
    if winner == "X":
        player_points[0] += 1
        showinfo("Finished", "Player One Win!")
    else:
        player_points[1] += 1
        showinfo("Finished", "Player Two Win!")


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