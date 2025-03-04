from analysis.filter import Filter
from policy.policy import Policy
from trader.real_trader import RealTrader
from trader.trader_exec import TraderExec
from trader.mock_trader import MockTrader
from task.task import Task
from seek.seek_akshare import Seek

if __name__ == '__main__':
    task = Task()
    seek = Seek()
    trader = RealTrader()
    traderExec = TraderExec(trader)
    filter = Filter()
    policy = Policy(filter)
    task.create_task(seek.real_data, 10)
    task.create_task(policy.top_rate_turnover_policy_day, 15)
    # task.create_task(traderExec.trader_stock, 20,
    #                  args=[policy.policy["rate_turnover_curday"]["name"]])
    task.start_task()
