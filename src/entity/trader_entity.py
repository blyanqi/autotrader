
class Balance():
    def __init__(self):
        # 参考市值
        self._amount = 0
        # 最大资产
        self._max_total = 10*10 ^ 8
        # '可用资金': 28494.21,
        # '币种': '0',
        # '总资产': 50136.21,
        # '资金余额': 28494.21,
        # '资金帐号': 'xxx'}

    @property
    def amount(self):
        return self._amount

    def deposit(self, value):
        if value < 0:
            raise ValueError("amount must be greater than 0")
        if value > self._max_total:
            raise ValueError("amount must be less than total")
        self._amount += value
        return self._amount

    def drawable(self, value):
        if value < 0:
            raise ValueError("amount must be greater than 0")
        if value > self._max_total:
            raise ValueError("amount must be less than total")
        if value > self._amount:
            raise ValueError("amount must be less than balance")
        self._amount -= value
        return self._amount
