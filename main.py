import tkinter as tk

window = tk.Tk()
window.title("XO Game")

def board():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_one = tk.Label(board_frame, text="player 1", font=("italic", 16), padx=10)
    label_player_two = tk.Label(board_frame, text="player 2", font=("italic", 16), padx=10)
    label_player_one.grid(row=0, column=0)
    label_player_two.grid(row=0, column=2)

board()
window.mainloop()