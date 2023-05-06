from flask import Blueprint, request
from stockfish import Stockfish
from config.config import AppConfig
import chess

bot = Blueprint('bot', __name__)
stockfish = Stockfish(path=AppConfig.stockfish_path)

@bot.route('/move', methods=['GET'])
def getMove():
	try:
		fen = request.args.get("fen")
		elo = request.args.get("elo")

		# initialize stockfish
		stockfish.set_depth(AppConfig.stockfish_depth)
		stockfish.set_elo_rating(elo)
		# initialize board
		board = chess.Board(fen)
		# sync player board with stockfish board
		stockfish.set_fen_position(board.fen())
		# set move to board
		botMove = stockfish.get_best_move()
		board.push_san(botMove)

		return {
			"fen": board.fen(),
			"move": botMove,
			"isCheckmate": board.is_check(),
			"isGameOver": board.is_game_over()
		}
	except Exception as e:
		print(e)
		return 'invalidMove', 400

@bot.route('/check-valid-move', methods=['GET'])
def isValid():
	try:
		fen = request.args.get("fen")
		playerMove = request.args.get("move")

		# initialize board
		board = chess.Board(fen)
		# player move
		board.push_uci(playerMove)

		return {
			"fen": board.fen(),
			"isValidMove": True,
			"isCheckmate": board.is_check(),
			"isGameOver": board.is_game_over()
		}, 200
	except Exception as e:
		return {
			"isValidMove": False
		}, 200
