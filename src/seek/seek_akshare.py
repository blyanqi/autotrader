import os
import akshare as ak
import pandas as pd
import datetime

pd.options = {
}


class Seek:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)

    def get_today(self):
        return datetime.datetime.now().strftime("%Y%m%d")

    def real_data(self):
        '''实时数据
        沪深京A股行情
        '''
        print("正在获取实时数据...")
        df = ak.stock_zh_a_spot_em()
        df.to_csv(
            f"{self.currentDir}/../data/real_data{self.get_today()}.csv", index=False)

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


if __name__ == '__main__':
    seek = Seek()
    seek.real_data()
    seek.real_data_with_bj()
    seek.real_data_with_sh()
    seek.real_data_with_se()
