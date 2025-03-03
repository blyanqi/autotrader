
from analysis.filter import Filter
from trader.trader_exec import TraderExec
from trader.mock_trader import MockTrader
from task.task import Task
from seek.seek_akshare import Seek

if __name__ == '__main__':
    task = Task()
    seek = Seek()
    traderExec = TraderExec()
    filter = Filter(traderExec)
    trader = MockTrader()
    seek.real_data()
    filter.filter_data()
    task.create_task(seek.real_data, 20)
    task.create_task(filter.filter_buy_stock, 10)
    task.create_task(filter.trader_filter_stock, 30, args=[trader])
    task.start_task()
