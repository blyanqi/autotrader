import os
import akshare as ak
import pandas as pd
import datetime

from core.logger import Logger

pd.options = {
}


class Seek:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)
        self.logger = Logger.get_logger("seek")

    def get_today(self):
        return datetime.datetime.now().strftime("%Y%m%d")

    def real_data(self):
        '''实时数据
        沪深京A股行情
        '''
        self.logger.info("-----------------正在获取实时数据-------------------")
        df = ak.stock_zh_a_spot_em()
        df.to_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", index=False)
        self.logger.info("-----------------正在获取实时数据 done -------------------")

    def real_data_with_sh(self):
        '''实时数据
        沪A股行情
        '''
        df = ak.stock_sh_a_spot_em()
        df.to_csv(
            f"{self.currentDir}/../data/real_data_sh{self.get_today()}.csv", index=False)

    def real_data_with_se(self):
        '''实时数据
        深A股行情
        '''
        df = ak.stock_sz_a_spot_em()
        df.to_csv(
            f"{self.currentDir}/../data/real_data_se{self.get_today()}.csv", index=False)

    def real_data_with_bj(self):
        '''实时数据
        京A股行情
        '''
        df = ak.stock_bj_a_spot_em()
        df.to_csv(
            f"{self.currentDir}/../data/real_data_bj{self.get_today()}.csv", index=False)

    def real_bid_info(self, code="000001"):
        df = ak.stock_bid_ask_em(symbol=code)

    def stock_info(self, code="000001"):
        df = ak.stock_individual_info_em(symbol=code)

    def history_data_of_day(self, code="000001"):
        df = ak.stock_zh_a_hist(symbol=code, period="daily",
                                start_date=self.get_today(), end_date=self.get_today(), adjust="")
        df.to_csv(
            f"{self.currentDir}/../data/hd_day{self.get_today()}.csv", index=False)

    def stock_intraday_em(self, code):
        df = ak.stock_intraday_em(symbol=code)
        df.to_csv(
            f"{self.currentDir}/../data/intraday{self.get_today()}.csv", index=False)
        return df


if __name__ == '__main__':
    seek = Seek()
    seek.stock_intraday_em("000001")
    # seek.real_data()
    # seek.real_data_with_bj()
    # seek.real_data_with_sh()
    # seek.real_data_with_se()
