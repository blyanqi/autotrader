
from pathlib import Path
from flask import Flask, render_template

from src.analysis.board import Board
from src.analysis.filter import Filter
# from src.seek.seek_akshare import Seek

app = Flask(__name__)


@app.route("/")
def hello_world():
    filter = Filter()
    return render_template('index.html', stocks=filter.test_filter().to_dict(orient="records"))


@app.route("/stock")
def hot_stock():
    board = Board()
    filter = Filter()
    return render_template('index.html', stocks=filter.test_filter().to_dict(orient="records"))
