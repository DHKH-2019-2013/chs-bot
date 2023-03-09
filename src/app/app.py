import chess
from stockfish import Stockfish

board = chess.Board()

stockfish = Stockfish(path="src/utils/stockfish/app.exe")
stockfish.set_depth(15)
stockfish.set_skill_level(10)

# player move
board.push_san("e4")
# sync player board with stockfish board
stockfish.set_fen_position(board.fen())
# set move to board
board.push_san(stockfish.get_best_move())

print(board)
