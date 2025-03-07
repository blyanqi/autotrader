# 定义一个接口
from abc import ABC, abstractmethod
import datetime


class TraderInf(ABC):
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def position(self):
        pass

    @abstractmethod
    def buy(self, code, num):
        pass

    @abstractmethod
    def sell(self, code):
        pass

    @abstractmethod
    def hold(self):
        pass

    def get_today(self):
        return datetime.datetime.now().strftime('%Y%m%d')
