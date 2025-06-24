# Create a tictactoe game for two players: human against bot
from tictactoe.game import Game
from tictactoe.bot import Bot
from tictactoe.ui import UI
def main():
    game = Game()
    bot = Bot(game)
    ui = UI(game)

    while not game.is_over():
        ui.display_board()
        if game.current_player == 'X':
            ui.get_player_move()
        else:
            bot.make_move()

    ui.display_board()
    ui.display_winner()

main()