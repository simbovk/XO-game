import tkinter as tk

window = tk.Tk()
window.title("XO Game")

def board():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    player_one_label = tk.Label(board_frame,text="player 1", font=("italic", 16), padx=10)
    player_two_label = tk.Label(board_frame,text="player 2", font=("italic", 16), padx=10)
    player_one_label.grid(row=0, column=0)
    player_two_label.grid(row=0, column=2)

    point_frame = tk.Frame(window)


board()
window.mainloop()