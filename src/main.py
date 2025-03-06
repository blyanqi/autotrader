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


def rate_volumnrate_policy_day(isTrader=False):
    task = Task()
    seek = Seek()
    trader = RealTrader()
    traderExec = TraderExec(trader)
    filter = Filter()
    policy = Policy(filter)
    task.create_task(seek.real_data, 10)
    task.create_task(policy.top_volumerate_day, 15)
    if isTrader:
        task.create_task(traderExec.trader_stock, 20,
                         args=[policy.policy["top_volumerate"]["name"]])
    task.start_task()


def sell_operator(rate):
    trader = RealTrader()
    traderExec = TraderExec(trader)
    stockHold = traderExec.hold()
    print(stockHold)
    count = 0
    for item in stockHold[1]:
        print(item)
        if item:
            if float(item) > rate:
                traderExec.sell(stockHold[0][count])
            count += 1
    pass


def test():
    trader = RealTrader()
    traderExec = TraderExec(trader)
    print(traderExec.sell("002276"))


def test2():
    seek = Seek()
    filter = Filter()
    print(filter.filter_stock_intraday_min("000001", seek))


if __name__ == '__main__':
    # rate_turnover_policy_day()
    # test()
    # sell_operator(5)
    rate_volumnrate_policy_day()
    pass
