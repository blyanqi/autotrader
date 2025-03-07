from trader.trader_inf import TraderInf


class MockTrader(TraderInf):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def balance(self):
        return "mock balance"

    def position(self):
        return "mock position"

    def buy(self, code, num):
        return f"mock buy {code}"

    def sell(self, code):
        return f"mock sell {code}"
