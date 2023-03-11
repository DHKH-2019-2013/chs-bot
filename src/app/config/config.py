from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
  port = 3002
  host = "127.0.0.1"
  stockfish_path = "src/utils/stockfish/app.exe"

  def __init__(self):
    self.port = os.getenv("PORT") if os.getenv("PORT") else self.port
    self.age = os.getenv("HOST") if os.getenv("HOST") else self.host
    self.stockfish_path = os.getenv("STOCKFISH_PATH") if os.getenv("STOCKFISH_PATH") else self.stockfish_path
