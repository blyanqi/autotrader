import datetime
import os
import pandas as pd
from io import StringIO

from src.analysis.filter import Filter
from src.entity.task_entity import JobCronEntity, JobEntity
from src.seek.seek_akshare import Seek
from src.task.task import Task

curDir = os.path.dirname(__file__)
# job4 = JobCronEntity()
# seek = Seek()
# task = Task()
# job4.name = "snapshot_real_data_10:33"
# job4.job = seek.snapshot_real_data
# job4.cron = "0 33 10 * * *"
# job4.args = ["10:33"]
# task.create_task_with_cron(job4)
# task.start_task()

df = pd.read_csv(
    f"{curDir}/src/data/real_data20250309.csv", dtype={"代码": str})
# df2 = pd.read_csv(
#     f"{curDir}/src/data/real_data20250306.csv", dtype={"代码": str})
# df2 = df2[["最高", "代码"]]
# print(df2)
# fdf = df[
#     (df["涨跌幅"] > 2)
#     & (df["涨跌幅"] < 20)
#     & (df["量比"] > 3)
#     & (df["60日涨跌幅"] <= 50)
#     & (df['最新价'] > df['今开'])
#     # & (df['最新价'] > df[''])
# ]
# dfm = pd.merge(fdf, df2, on="代码")
# # print(dfm)
# fdf = dfm[dfm["最高_y"] < dfm["最新价"]]
# print(fdf)


if __name__ == "__main__":
    filter = Filter()
    print(filter.get_trader_before_day())
