import logging
from core.container import IoCContainer
import core.service as service


def rate_volumnrate_policy_day(isTrader=False):
    container = IoCContainer()
    task = container.resolve("task")
    seek = container.resolve("seek")
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    filter = container.resolve("filter")
    policy = container.resolve("policy", filter)
    task.create_task(seek.real_data, 10)
    task.create_task(policy.top_volumerate_day, 15)
    if isTrader:
        task.create_task(traderExec.trader_stock, 20,
                         args=[policy.policy["top_volumerate"]["name"]])
    task.start_task()


if __name__ == '__main__':
    # rate_turnover_policy_day()
    # test()
    # sell_operator(5)
    rate_volumnrate_policy_day(True)
    pass
