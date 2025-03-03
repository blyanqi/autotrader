
import datetime
import os

import pandas as pd


class Board:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)

    def get_today(self):
        return datetime.datetime.now().strftime("%Y%m%d")

    def get_today_board(self):
        boardInfo = {}
        boardInfo["大盘上涨家数"] = 200
        boardInfo["大盘下涨家数"] = 200
        boardInfo["大盘上涨5%家数"] = 200
        boardInfo["大盘涨停家数"] = 200
        boardInfo["大盘成交额家数"] = 200
        boardInfo["大盘10日涨幅"] = 0.3
        boardInfo["大盘20日涨幅"] = 0.2
        boardInfo["大盘30日涨幅"] = 0.1
        boardInfo["大盘60日涨幅"] = 0.05
        return boardInfo

    def get_hot_stock(self):
        df = pd.read_csv(os.path.join(
            self.currentDir, f"../data/filter_rate{self.get_today()}.csv"), dtype={"代码": str})
        return df.to_dict(orient="records")
