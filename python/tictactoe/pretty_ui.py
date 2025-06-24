# Create a pretty UI by using tkinter or another GUI library for Tic Tac Toe
import tkinter as tk
from tictactoe.game import Game
from tictactoe.bot import Bot
from tictactoe.ui import UI

class PrettyUI(UI):
    def __init__(self, game: Game):
        super().__init__(game)
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [None] * 9
        self.create_buttons()
        self.status_label = tk.Label(self.window, text="")
        self.status_label.pack()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.window, text=' ', font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button

    def on_button_click(self, position):
        if self.game.board[position] == ' ' and self.game.winner is None:
            self.game.make_move(position)
            self.update_buttons()
            if not self.game.is_over():
                bot = Bot(self.game)
                bot.make_move()
                self.update_buttons()
            self.check_game_status()

    def update_buttons(self):
        for i in range(9):
            self.buttons[i].config(text=self.game.board[i])

    def check_game_status(self):
        if self.game.winner:
            self.status_label.config(text=f"Player {self.game.winner} wins!")
        elif ' ' not in self.game.board:
            self.status_label.config(text="It's a draw!")
        else:
            current_player = 'X' if self.game.current_player == 'X' else 'O'
            self.status_label.config(text=f"Current Player: {current_player}")

    def run(self):
        self.window.mainloop()
