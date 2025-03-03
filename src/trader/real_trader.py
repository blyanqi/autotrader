from trader.trader_inf import TraderInf


class RealTrader(TraderInf):
    def __init__(self):
        pass

    def balance(self):
        return "real balance"

    def position(self):
        return "real position"

    def buy(self, code):
        return f"real buy {code}"

    def sell(self, code):
        return f"real sell {code}"
