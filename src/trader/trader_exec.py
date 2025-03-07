import datetime
import json
import logging
import math
import os

import pandas as pd
from trader.trader_inf import TraderInf


class TraderExec:
    def __init__(self, trader: TraderInf):
        self.currentDir = os.path.dirname(__file__)
        self._trader = trader  # 交易系统
        self._amount = 20000    # 入市金额
        self._buyList = {}      # 今日交易的股票池
        self._holdtake = 2     # hold stock
        self._bottle = 5        # 份额
        self.isTrader = False
        self.logger = logging.getLogger("trader_exec")
        self.load_buy_list()

    def get_today(self):
        return datetime.datetime.now().strftime('%Y%m%d')

    def balance(self):
        return self._trader.balance()

    def position(self):
        return self._trader.position()

    def buy(self, code, num):
        return self._trader.buy(code, num)

    def sell(self, code):
        return self._trader.sell(code)

    def get_time(self):
        time = datetime.datetime.now().time()
        return time

    def load_buy_list(self):
        try:
            self._buyList = json.load(open(
                f"{self.currentDir}/../data/buyList_{self.get_today()}.json", "r"))
        except Exception as e:
            print(e)
            pass

    def add_buy_list(self, record):
        try:
            self._buyList[record["code"]] = record
            json.dump(self._buyList, open(
                f"{self.currentDir}/../data/buyList_{self.get_today()}.json", "w"))
        except:
            pass

    def get_timezone(self):
        if self.get_time() <= datetime.time(9, 35):
            return "09:35"
        if self.get_time() <= datetime.time(9, 45):
            return "09:45"
        if self.get_time() <= datetime.time(10, 00):
            return "10:00"
        return "other"

    def trader_stock(self, policyName):
        df = pd.read_csv(
            f"{self.currentDir}/../data/{policyName}{self.get_today()}_{self.get_timezone()}.csv", dtype={"代码": str})
        if df.empty:
            return
        traderData = df.head(self._holdtake).to_dict(orient='records')
        for row in traderData:
            if len(self._buyList) >= self._holdtake:
                return
            code = row["代码"]
            if code in self._buyList:
                continue
            price = row["最新价"]
            num = math.floor(self._amount/self._bottle/price/100)*100
            self.logger.info("trader: ", code, price, num)
            self.add_buy_list({"code": code, "price": price, "num": num})
            if self.isTrader:
                self.buy(code, num)

    def hold(self):
        print("get hold stock")
        holdstock = self._trader.hold()
        holdstock = holdstock.replace(",", "")
        stockInfo = holdstock.split("\n")
        stockList = stockInfo[:5]
        stockRate = stockInfo[5:]
        return [stockList, stockRate]


if __name__ == '__main__':
    from src.trader.mock_trader import MockTrader
    # from src.trader.real_trader import RealTrader
    trader = MockTrader()
    trader_exec = TraderExec(trader)
    print(trader_exec.get_today())
    print(trader_exec.buy())
    print(trader_exec.sell())
