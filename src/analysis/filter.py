import os
import time
import pandas as pd
import datetime


class Filter:
    def __init__(self, traderExec):
        self.currentDir = os.path.dirname(__file__)
        self.buyList = []
        self.traderExec = traderExec

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def filter_data(self):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[df["涨跌幅"] > 9]["代码"]
        fdf.to_csv(
            f"{self.currentDir}/../data/filter_rate{self.get_today()}.csv", index=False)

    def filter_buy_stock(self):
        print("filter buy stock")
        df = pd.read_csv(
            f"{self.currentDir}/../data/filter_rate{self.get_today()}.csv", dtype={"代码": str})
        alldf = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        filterDf = pd.merge(df, alldf, on="代码")
        # print(filterDf)
        filterDf = filterDf[(filterDf["换手率"] > 30) & (
            filterDf["涨跌幅"] < 5) & (filterDf["涨跌幅"] > 2)]
        filterDf.to_csv(
            f"{self.currentDir}/../data/filter_buy_stock{self.get_today()}.csv", index=False)

    def trader_filter_stock(self, trader):
        df = pd.read_csv(
            f"{self.currentDir}/../data/filter_buy_stock{self.get_today()}.csv", dtype={"代码": str})
        if df["代码"].empty:
            return
        codes = df["代码"]
        # print(df["代码"])
        for code in codes:
            if code in self.buyList:  # 防止重复购买
                return
            if len(self.buyList) > 3:  # 购买股票数量限制
                return
            print(code)
            self.buyList.append(code)
            print(self.traderExec(trader).buy(code))
            time.sleep(20)


if __name__ == '__main__':
    filter = Filter(None)
    filter.filter_data()
