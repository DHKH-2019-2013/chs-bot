from flask import Blueprint
from stockfish import Stockfish
from config.config import AppConfig
import chess

bot = Blueprint('bot', __name__)

@bot.route('')
def show():
	# board = chess.Board()

	# stockfish = Stockfish(path=AppConfig.stockfish_path)
	# stockfish.set_depth(15)
	# stockfish.set_skill_level(10)

	# # player move
	# board.push_san("e4")
	# # sync player board with stockfish board
	# stockfish.set_fen_position(board.fen())
	# # set move to board
	# board.push_san(stockfish.get_best_move())

	return "Hello, I am stockfish"
