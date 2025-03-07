
from config.config import ConfigLoader
from config.config_filesystem import ConfigReloadHandler
from .container import IoCContainer
from analysis.filter import Filter
from .logger import Logger
from policy.policy import Policy
from seek.seek_akshare import Seek
from task.task import Task
from trader.real_trader import RealTrader
from trader.trader_exec import TraderExec

container = IoCContainer()

container.register("realTrader", RealTrader, singleton=True)
container.register("task", Task, singleton=True)
container.register("seek", Seek, singleton=True)
container.register("traderExec", TraderExec, singleton=True)
container.register("filter", Filter, singleton=True)
container.register("policy", Policy, singleton=True)
container.register("config", ConfigLoader, singleton=True)
container.register("configReload", ConfigReloadHandler, singleton=True)
