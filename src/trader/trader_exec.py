import datetime
import os
import time

import pandas as pd

from trader.trader_inf import TraderInf


class TraderExec:
    def __init__(self, trader: TraderInf):
        self.currentDir = os.path.dirname(__file__)
        self._trader = trader
        self._buyList = []

    def get_today(self):
        return datetime.datetime.now().strftime('%Y%m%d')

    def balance(self):
        return self._trader.balance()

    def position(self):
        return self._trader.position()

    def buy(self, code):
        return self._trader.buy(code)

    def sell(self, code):
        return self._trader.sell(code)

    def get_time(self):
        time = datetime.datetime.now().time()
        return time

    def get_timezone(self):
        print(self.get_time())
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
        if df["代码"].empty:
            return
        codes = df["代码"]
        # print(df["代码"])
        for code in codes:
            if code in self._buyList:  # 防止重复购买
                return
            if len(self._buyList) >= 3:  # 购买股票数量限制
                return
            print("trader: ", code)
            self._buyList.append(code)
            print(self.buy(code))
            time.sleep(20)


if __name__ == '__main__':
    from src.trader.mock_trader import MockTrader
    # from src.trader.real_trader import RealTrader
    trader = MockTrader()
    trader_exec = TraderExec(trader)
    print(trader_exec.get_today())
    print(trader_exec.buy())
    print(trader_exec.sell())
