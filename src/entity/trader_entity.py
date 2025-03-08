
class Balance():

    def __init__(self):
        # 资产总值
        self._amount = 0
        # 净资产
        self._netAsset = 0
        # 总市值
        self._marketValue = 0
        # 可用
        self._useable = 0
        # 可取
        self._drawable = 0

    @property
    def amount(self):
        return self._amount

    @property
    def netAsset(self):
        return self._netAsset

    @property
    def marketValue(self):
        return self._marketValue

    @property
    def useable(self):
        return self._useable

    @property
    def drawable(self):
        return self._drawable

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @netAsset.setter
    def netAsset(self, netAsset):
        self._netAsset = netAsset

    @marketValue.setter
    def marketValue(self, marketValue):
        self._marketValue = marketValue

    @useable.setter
    def useable(self, useable):
        self._useable = useable

    @drawable.setter
    def drawable(self, drawable):
        self._drawable = drawable


if __name__ == "__main__":
    balance = Balance()
    print(balance.amount)
    balance.amount = 100
    print(balance.amount)
