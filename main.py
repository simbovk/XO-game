import tkinter as tk

window = tk.Tk()
window.title("XO Game")

def points():
    name_frame = tk.Frame(window)
    name_frame.grid(row=0)
    player_one_label = tk.Label(name_frame, text="player 1", font=("None", 16, "italic"), padx=10)
    player_two_label = tk.Label(name_frame, text="player 2", font=("None", 16, "italic"), padx=10)
    player_one_label.grid(row=0, column=0)
    player_two_label.grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    player_one_point = tk.Label(point_frame, text="0", font=("None", 16, "italic"), padx=20)
    player_two_point = tk.Label(point_frame, text="0", font=("None", 16, "italic"), padx=20)
    player_one_point.grid(row=0, column=0)
    player_two_point.grid(row=0, column=1)

def board():
    buttons = []
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    counter = 0
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame)
            buttons[index].config(width=10, height=4, font=("None", 18, "bold"))
            buttons[index].grid(row=row, column=column)
            counter += 1

points()
board()

window.mainloop()