import os
import time
import pandas as pd
import datetime


class Filter:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def get_yestoday(self):
        yestoday = (datetime.datetime.now() -
                    datetime.timedelta(days=1)).strftime("%Y%m%d")
        return yestoday

    def filter_data(self, inDate):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_yestoday()}.csv", dtype={"代码": str})
        fdf = df[df["涨跌幅"] > 9]["代码"]
        fdf.to_csv(
            f"{self.currentDir}/../data/filter_rate{inDate}.csv", index=False)

    def filter_top_with_rate_turnover(self, min_rate, max_rate, turnover, filename):
        df = pd.read_csv(
            f"{self.currentDir}/../data/filter_rate{self.get_yestoday()}.csv", dtype={"代码": str})
        alldf = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        filterDf = pd.merge(df, alldf, on="代码")
        # print(filterDf)
        filterDf = filterDf[(filterDf["换手率"] >= min_rate) & (
            filterDf["涨跌幅"] <= max_rate) & (filterDf["涨跌幅"] >= turnover)]
        filterDf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)

    def filter_with_turnover(self, min_rate, max_rate, turnover, filename):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > min_rate) & (df["涨跌幅"] < max_rate)
                 & (df["换手率"] > turnover) & (df["60日涨跌幅"] < 30)]
        fdf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)

    def test_filter(self):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > 2) & (df["涨跌幅"] < 5)
                 & (df["换手率"] > 20)]
        return fdf[["代码", "名称", "涨跌幅", "换手率"]]


if __name__ == '__main__':
    filter = Filter()
    # print(filter.get_yestoday())
    print(filter.filter_data(filter.get_yestoday()))
