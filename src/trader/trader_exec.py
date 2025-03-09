import re
import time
from src.entity.trader_entity import Balance
from src.trader.trader_inf import TraderInf
from src.config.config import ConfigLoader
from src.core.logger import Logger
import pandas as pd
import os
import math
import json
import datetime


class TraderExec:
    def __init__(self, trader: TraderInf):
        config = ConfigLoader()
        self.currentDir = os.path.dirname(__file__)
        self.logger = Logger.get_logger("trader_exec")
        self._trader = trader
        # 配置
        self._isTrader = config.get(
            "trader.is_trader")
        self._amount = config.get("trader.amount")
        self._holdtake = config.get("trader.holdtake")
        self._bottle = config.get("trader.bottle")
        self._banTraderFailedCount = config.get(
            "trader.ban_trader_failed_count")
        self.max_holdtake = config.get("trader.max_holdtake")
        self.max_hold_amount = config.get("trader.max_hold_amount")
        # 运行时
        self._buyList = {}
        self._traderFailedCount = 0
        self.balance = Balance()
        # 加载
        self.load_buy_list()
        self.get_balance()

    def get_today(self):
        return datetime.datetime.now().strftime('%Y%m%d')

    def get_balance(self):
        try:
            resInfo = self._trader.balance()
            if resInfo is None:
                self.logger.info(f"balance: {resInfo}")
                return
            resInfo = resInfo.replace(",", "")
            self.logger.info(f"trader: {resInfo}")
            pattern = r'(\w+):\s+([\d,\.]+)'
            fields = re.findall(pattern, resInfo)
            if fields is not None:
                fields_dict = {k: v.replace(',', '') for k, v in fields}
            else:
                pattern = r'(\w+)\.\s+([\d,\.]+)'
                fields = re.findall(pattern, resInfo)
                if fields is None:
                    return
                fields_dict = {k: v.replace(',', '') for k, v in fields}
            self.balance.amount = float(fields_dict['资产总值'])
            self.balance.netAsset = float(fields_dict['净资产'])
            self.balance.marketValue = float(fields_dict['总市值'])
            self.balance.useable = float(fields_dict['可用'])
            self.balance.drawable = float(fields_dict['可取'])
        except:
            self.logger.info(f"balance error")

    def position(self):
        return self._trader.position()

    def get_time(self):
        time = datetime.datetime.now().time()
        return time

    def load_buy_list(self):
        try:
            if os.path.exists(f"{self.currentDir}/../data/buyList_{self.get_today()}.json"):
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

    def trader_process(self):
        self.logger.info(
            f"----------------------Trader start-----------------------")
        if not self._isTrader:
            self.logger.info("trader is not open")
            return False
        if len(self._buyList) >= self.max_holdtake:
            self.logger.info("hold stock is full")
            return False

        if self.balance.amount == 0:
            self.logger.info("balance is zero")
            return False

        if self.balance.marketValue >= self.max_hold_amount:
            self.logger.info("hold amount is full")
            return False
        return True

    def policy_buy_stock(self, policyName):
        if not self.trader_process():
            return
        if not os.path.exists(f"{self.currentDir}/../data/{policyName}{self.get_today()}_{self.get_timezone()}.csv"):
            self.logger.info("no trader data")
            return
        df = pd.read_csv(
            f"{self.currentDir}/../data/{policyName}{self.get_today()}_{self.get_timezone()}.csv", dtype={"代码": str})
        if df.empty:
            return
        traderData = df.head(self._holdtake).to_dict(orient='records')
        for row in traderData:
            code = row["代码"]
            if code in self._buyList:
                continue
            if self._traderFailedCount >= self._banTraderFailedCount:
                self.logger.info(
                    f"trader failed count: {self._traderFailedCount}")
                return
            price = row["最新价"]
            num = math.floor(self._amount/self._bottle/price/100)*100
            if num <= 0:
                continue
            self.logger.info(f"trader: {code}, {price}, {num}")
            self._trader.buy(code, num)
            self.add_buy_list({"code": code, "price": price, "num": num})

    def get_hold(self):
        holdstock = self._trader.hold()
        self.logger.info(f"hold stock: {holdstock}")
        if not holdstock:
            return []
        stockInfo = holdstock.split(",")
        self.logger.debug(f"{stockInfo}")
        stockList = stockInfo[0].removesuffix("\n").split("\n")
        stockRate = stockInfo[1].removesuffix("\n").split("\n")
        stockHoldNum = stockInfo[2].removesuffix("\n").split("\n")
        return [stockList, stockRate, stockHoldNum]

    def sell_all(self):
        holdStock = self.get_hold()
        self.logger.info(f"hold stock: {holdStock}")
        stockList = holdStock[0]
        self.logger.debug(f"{stockList}")
        for stock in stockList:
            self._trader.sell_all(stock)

    def sell_that(self):
        holdStock = self.get_hold()
        self.logger.info(f"hold stock: {holdStock}")
        stockList = holdStock[0]
        stockNum = holdStock[2]
        self.logger.debug(f"{stockList} {stockNum}")
        for index in range(len(stockList)):
            self.logger.info(f"{stockList[index]} {stockNum[index]}")
            self._trader.sell(stockList[index], stockNum[index])
            time.sleep(1)

    def buy(self, code, num):
        if len(code) != 6:
            self.logger.info(f"code error: {code}")
            return
        if int(num) > 10000:
            self.logger.info(f"num error: {num}")
            return
        self._trader.buy(code, num)

    def sell(self, code, num):
        if len(code) != 6:
            self.logger.info(f"code error: {code}")
            return
        if int(num) > 10000:
            self.logger.info(f"num error: {num}")
            return
        self._trader.sell(code, num)

    def test(self, code, num):
        pass


if __name__ == '__main__':
    from src.trader.mock_trader import MockTrader
    # from src.trader.real_trader import RealTrader
    trader = MockTrader()
    trader_exec = TraderExec(trader)
    print(trader_exec.get_today())
    print(trader_exec.buy())
    print(trader_exec.sell())
