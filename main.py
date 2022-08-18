import tkinter as tk

window = tk.Tk()
window.title("XO Game")

def board():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    player_one_label = tk.Label(board_frame, text="player 1", font=("Italic", 16), padx=10)
    player_two_label = tk.Label(board_frame, text="player 2", font=("Italic", 16), padx=10)
    player_one_label.grid(row=0, column=0)
    player_two_label.grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    player_one_point = tk.Label(point_frame, text="0", font=("Italic", 16), padx=20)
    player_two_point = tk.Label(point_frame, text="0", font=("Italic", 16), padx=20)
board()
window.mainloop()