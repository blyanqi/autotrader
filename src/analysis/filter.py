import logging
import os
import time
import pandas as pd
import datetime


class Filter:
    def __init__(self, seek):
        self.currentDir = os.path.dirname(__file__)
        self.seek = seek
        self.logger = logging.getLogger(__name__)

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def get_yestoday(self):
        yestoday = (datetime.datetime.now() -
                    datetime.timedelta(days=1)).strftime("%Y%m%d")
        return yestoday

    def filter_data(self, inDate):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{inDate}.csv", dtype={"代码": str})
        fdf = df[df["涨跌幅"] > 9]["代码"]
        fdf.to_csv(
            f"{self.currentDir}/../data/filter_rate{inDate}.csv", index=False)

    def filter_top_with_rate_turnover(self, min_rate, max_rate, turnover, filename):
        df = pd.read_csv(
            f"{self.currentDir}/../data/filter_rate{self.get_yestoday()}.csv", dtype={"代码": str})
        alldf = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        filterDf = pd.merge(df, alldf, on="代码")
        filterDf = filterDf[(filterDf["换手率"] >= turnover) & (
            filterDf["涨跌幅"] <= max_rate) & (filterDf["涨跌幅"] >= min_rate)
            & (df["60日涨跌幅"] < 50)].head(1)
        filterDf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)

    def filter_with_turnover(self, min_rate, max_rate, turnover, filename):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > min_rate) & (df["涨跌幅"] < max_rate)
                 & (df["换手率"] > turnover) & (df["60日涨跌幅"] < 30)].head(1)
        fdf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)

    def is_valid(self, row):
        # 如果出发地和目的地相同，则返回 False
        return row['最新价'] > row['今开']

    def filter_with_volumerate(self, min_rate, max_rate, volumerate, filename):
        fdf = pd.DataFrame()
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > min_rate) & (df["涨跌幅"] < max_rate)
                 & (df["量比"] > volumerate) & (df["60日涨跌幅"] <= 55)]
        # fdf = df[(df["涨跌幅"] > min_rate) & (df["涨跌幅"] < max_rate)
        #          & (df["量比"] > volumerate) & (df["60日涨跌幅"] <= 55)]
        fdf = fdf[fdf.apply(self.is_valid, axis=1)]
        if fdf.empty:
            return
        self.logger.info("-----------------写入分析数据-------------------")
        fdf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)
        self.logger.info("-----------------写入分析数据 done -------------------")

    def filter_rate(self):
        df = pd.read_csv(
            f"{self.currentDir}/../data/filter_rate{self.get_yestoday()}.csv", dtype={"代码": str})
        alldf = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        filterDf = pd.merge(df, alldf, on="代码")
        filterDf = filterDf[(filterDf["涨跌幅"] >= 9) & (filterDf["60日涨跌幅"] < 50)]
        filterDf.to_csv(
            f"{self.currentDir}/../data/filter_rate.csv", index=False)

    def filter_stock_intraday_min(self, row):
        try:
            df = self.seek.stock_intraday_em(row["代码"])
            filtered_df = df[df['时间'].str.startswith('09:30')]
            openPrice = filtered_df.iloc[0]["成交价"]
            currPrice = df.tail(1)[["成交价"]].values[0]
            return openPrice < currPrice
        except:
            return False

    def test_filter(self):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > 2) & (df["涨跌幅"] < 5)
                 & (df["换手率"] > 20)]
        return fdf[["代码", "名称", "涨跌幅", "换手率"]]


if __name__ == '__main__':
    filter = Filter()
    # print(filter.get_yestoday())
    # print(filter.filter_data(filter.get_today()))
