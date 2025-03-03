
from pathlib import Path
from flask import Flask, render_template

from src.analysis.board import Board
# from src.seek.seek_akshare import Seek

app = Flask(__name__)


@app.route("/")
def hello_world():
    board = Board()
    return render_template('index.html', board=board.get_hot_stock()[0])


@app.route("/stock")
def hot_stock():
    board = Board()
    return render_template('hot_stock.html', stocks=board.get_hot_stock())
