import datetime

from entity.trader_entity import Balance
from trader.trader_inf import TraderInf


class TraderExec:
    def __init__(self, trader: TraderInf):
        self._trader = trader
        # self._balance = balance

    def get_today(self):
        return datetime.datetime.now().strftime('%Y%m%d')

    def balance(self):
        return self._trader.balance()

    def position(self):
        return self._trader.position()

    def buy(self, code):
        return self._trader.buy(code)

    def sell(self, code):
        return self._trader.sell(code)


if __name__ == '__main__':
    from src.trader.mock_trader import MockTrader
    # from src.trader.real_trader import RealTrader
    trader = MockTrader()
    trader_exec = TraderExec(trader)
    print(trader_exec.get_today())
    print(trader_exec.buy())
    print(trader_exec.sell())
