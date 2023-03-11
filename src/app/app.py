from flask import Flask
from config.config import AppConfig
from controllers.bot import bot
from controllers.health_check import health_check

app = Flask(__name__)

app.register_blueprint(bot)
app.register_blueprint(health_check)

app.run(host=AppConfig.host, port=AppConfig.port)
