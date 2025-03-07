import os
from core.container import IoCContainer
import core.service as service
from watchdog.observers import Observer

curDir = os.path.dirname(__file__)
container = IoCContainer()
config = container.resolve("config", f"{curDir}/config/config.yaml")
event_handler = container.resolve("configReload", config)
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()


def rate_volumnrate_policy_day(isTrader=False):
    type1 = config.get_nested_value("policy.0")
    task = container.resolve("task")
    seek = container.resolve("seek")
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    filter = container.resolve("filter")
    policy = container.resolve("policy", filter)
    task.create_task(config.get("task.real_data.name"),
                     seek.real_data,
                     config.get("task.real_data.timer"))
    task.create_task(config.get("task.policy_top.name"),
                     policy.top_volumerate_day,
                     config.get("task.policy_top.timer"))
    if isTrader:
        task.create_task(config.get("task.trader.name"),
                         traderExec.trader_stock,
                         config.get("task.trader.timer"),
                         args=[type1["name"]])
    task.start_task()


if __name__ == '__main__':
    rate_volumnrate_policy_day(True)
    pass
