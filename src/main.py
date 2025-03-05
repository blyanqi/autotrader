from analysis.filter import Filter
from policy.policy import Policy
from trader.real_trader import RealTrader
from trader.trader_exec import TraderExec
from trader.mock_trader import MockTrader
from task.task import Task
from seek.seek_akshare import Seek


def rate_turnover_policy(isTrader=False):
    task = Task()
    seek = Seek()
    trader = RealTrader()
    traderExec = TraderExec(trader)
    filter = Filter()
    policy = Policy(filter)
    task.create_task(seek.real_data, 10)
    task.create_task(policy.top_rate_turnover_policy, 15)
    if isTrader:
        task.create_task(traderExec.trader_stock, 20,
                         args=[policy.policy["rate_turnover"]["name"]])
    task.start_task()


def rate_turnover_policy_day(isTrader=False):
    task = Task()
    seek = Seek()
    trader = RealTrader()
    traderExec = TraderExec(trader)
    filter = Filter()
    policy = Policy(filter)
    task.create_task(seek.real_data, 10)
    task.create_task(policy.top_rate_turnover_policy_day, 15)
    if isTrader:
        task.create_task(traderExec.trader_stock, 20,
                         args=[policy.policy["rate_turnover_curday"]["name"]])
    task.start_task()


def test():
    trader = RealTrader()
    traderExec = TraderExec(trader)
    print(traderExec.sell("000001"))


if __name__ == '__main__':
    rate_turnover_policy()
    pass
