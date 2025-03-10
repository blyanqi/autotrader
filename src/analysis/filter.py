import os
import pandas as pd
import datetime

from src.core.logger import Logger


class Filter:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)
        self.logger = Logger.get_logger("filter")

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def get_trader_day(self):
        today = datetime.date.today()
        weekday = today.weekday()
        if weekday == 5:
            return datetime.date.today() - datetime.timedelta(days=1)
        elif weekday == 6:
            return datetime.date.today() - datetime.timedelta(days=2)
        else:
            return today

    def get_trader_before_day(self):
        resDay = ""
        today = datetime.date.today()
        weekday = today.weekday()
        if weekday == 5:
            resDay = datetime.date.today() - datetime.timedelta(days=2)
        elif weekday == 6:
            resDay = datetime.date.today() - datetime.timedelta(days=3)
        elif weekday == 0:
            resDay = datetime.date.today() - datetime.timedelta(days=3)
        else:
            resDay = today - datetime.timedelta(days=1)
        resDay = resDay.strftime("%Y%m%d")
        return resDay

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
        return row['最新价'] > row['今开']

    def filter_with_volumerate_of_before_day(self, min_rate, max_rate, volumerate, day60rate, filename):
        self.logger.info(
            "-----------------filter_with_volumerate-------------------")
        self.logger.info(f'''min_rate: {min_rate}''')
        self.logger.info(f'''max_rate: {max_rate}''')
        self.logger.info(f'''volumerate: {volumerate}''')
        self.logger.info(f'''day60rate: {day60rate}''')
        self.logger.info(f'''filename: {filename}''')
        fdf = pd.DataFrame()
        df_before = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_trader_before_day()}.csv", dtype={"代码": str})
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        df_before = df_before[["最高", "代码"]]
        fdf = df[
            (df["涨跌幅"] > min_rate)
            & (df["涨跌幅"] < max_rate)
            & (df["量比"] > volumerate)
            & (df["60日涨跌幅"] <= day60rate)
            & (df['最新价'] > df['今开'])
        ]
        dfm = pd.merge(fdf, df_before, on="代码")
        fdf = dfm[dfm["最高_y"] < dfm["最新价"]]
        if fdf.empty:
            return
        fdf = fdf.sort_values(by="量比", ascending=False)
        fdf.to_csv(
            f"{self.currentDir}/../data/{filename}.csv", index=False)
        self.logger.info("-----------------写入分析数据 done -------------------")

    def filter_with_volumerate(self, min_rate, max_rate, volumerate, day60rate, filename):
        self.logger.info(
            "-----------------filter_with_volumerate-------------------")
        self.logger.info(f'''min_rate: {min_rate}''')
        self.logger.info(f'''max_rate: {max_rate}''')
        self.logger.info(f'''volumerate: {volumerate}''')
        self.logger.info(f'''day60rate: {day60rate}''')
        self.logger.info(f'''filename: {filename}''')
        fdf = pd.DataFrame()
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[
            (df["涨跌幅"] > min_rate)
            & (df["涨跌幅"] < max_rate)
            & (df["量比"] > volumerate)
            & (df["60日涨跌幅"] <= day60rate)
            & (df['最新价'] > df['今开'])
        ]
        # fdf = fdf[fdf.apply(self.is_valid, axis=1)]
        if fdf.empty:
            return
        fdf = fdf.sort_values(by="量比", ascending=False)
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

    def test_filter(self):
        df = pd.read_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", dtype={"代码": str})
        fdf = df[(df["涨跌幅"] > 2) & (df["涨跌幅"] < 5)
                 & (df["换手率"] > 20)]
        return fdf[["代码", "名称", "涨跌幅", "换手率"]]


if __name__ == '__main__':
    filter = Filter()
    print(filter.get_trader_day())
    # print(filter.filter_data(filter.get_today()))
