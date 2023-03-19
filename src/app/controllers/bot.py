from flask import Blueprint, request
from stockfish import Stockfish
from config.config import AppConfig
import chess

bot = Blueprint('bot', __name__)
stockfish = Stockfish(path=AppConfig.stockfish_path)

@bot.route("/initialize-chess-board", methods=['GET'])
def getInitializeChessBoard():
	board = chess.Board()
	return board.fen()

@bot.route('/move', methods=['GET'])
def getMove():
	try:
		fen = request.args.get("fen")
		playerMove = request.args.get("move")
		int = request.args.get("int")

		stockfish.set_depth(AppConfig.stockfish_depth)
		stockfish.set_skill_level(int)

		board = chess.Board(fen)
		# player move
		move = chess.Move.from_uci(playerMove)
		board.push_san(board.san(move))
		# sync player board with stockfish board
		stockfish.set_fen_position(board.fen())
		# set move to board
		botMove = stockfish.get_best_move()
		board.push_san(botMove)

		return {
			"fen": board.fen(),
			"move": botMove,
			"isCheckmate": board.is_checkmate()
		}
	except Exception as e:
		print(e)
		return 'invalidMove', 400
