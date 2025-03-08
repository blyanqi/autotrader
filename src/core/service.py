
from src.config.config import ConfigLoader
from src.config.config_filesystem import ConfigReloadHandler
from .container import IoCContainer
from src.analysis.filter import Filter
from .logger import Logger
from src.policy.policy import Policy
from src.seek.seek_akshare import Seek
from src.task.task import Task
from src.trader.real_trader import RealTrader
from src.trader.trader_exec import TraderExec

container = IoCContainer()

container.register("realTrader", RealTrader, singleton=True)
container.register("task", Task, singleton=True)
container.register("seek", Seek, singleton=True)
container.register("traderExec", TraderExec, singleton=True)
container.register("filter", Filter, singleton=True)
container.register("policy", Policy, singleton=True)
container.register("config", ConfigLoader, singleton=True)
container.register("configReload", ConfigReloadHandler, singleton=True)
