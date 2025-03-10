import os
from src.core.container import IoCContainer
import src.core.service as service
from watchdog.observers import Observer
from src.entity.task_entity import JobCronEntity, JobEntity

curDir = os.path.dirname(__file__)
container = IoCContainer()
config = container.resolve("config", f"{curDir}/src/config/config.yaml")
event_handler = container.resolve("configReload", config)
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()


def sell_all_trader():
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    traderExec.sell_all()


def sell_all_rate(rate):
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    traderExec.sell_all_rate(rate)


if __name__ == '__main__':
    sell_all_trader()
    # sell_all_rate(1)
    pass
