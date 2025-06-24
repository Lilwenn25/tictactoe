# Here we handle the UI display for Tic Tac Toe
from tictactoe.game import Game

class UI:
    def __init__(self, game: Game):
        self.game = game

    def display_board(self):
        print("\nCurrent Board:")
        for i in range(3):
            print(" | ".join(self.game.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 9)
        print()

    def get_player_move(self):
        while True:
            try:
                move = int(input(f"Player {self.game.current_player}, enter your move (0-8): "))
                if move < 0 or move > 8 or self.game.board[move] != ' ':
                    raise ValueError
                self.game.make_move(move)
                break
            except ValueError:
                print("Invalid move. Please try again.")

    def display_winner(self):
        if self.game.winner:
            print(f"Player {self.game.winner} wins!")
        else:
            print("It's a draw!")