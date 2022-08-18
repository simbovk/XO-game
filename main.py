import tkinter as tk

window = tk.Tk()
window.title("XO Game")

def board():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_one = tk.Label(board_frame, text="player1", font=("Aviny", 16), padx=10)
    label_player_two = tk.Label(board_frame, text="player2", font=("Aviny", 16), padx=10)

window.mainloop()