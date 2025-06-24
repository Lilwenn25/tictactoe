# Here we handle the bot logic for Tic Tac Toe
from tictactoe.game import Game
import random

class Bot:
    def __init__(self, game: Game):
        self.game = game

    def make_move(self):
        move = self.smart_move()
        if move is not None:
            self.game.make_move(move)
            return

        available_moves = [i for i, cell in enumerate(self.game.board) if cell == ' ']
        if available_moves:
            move = random.choice(available_moves)
            self.game.make_move(move)
    
    # MAke the bot smarter by implementing a simple strategy
    def smart_move(self):
        # Check if the bot can win in the next move
        for i in range(9):
            if self.game.board[i] == ' ':
                self.game.board[i] = 'O'
                if self.game.check_winner():
                    return i
                self.game.board[i] = ' '
        return None