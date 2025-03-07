import logging
import os
import subprocess
from trader.trader_inf import TraderInf
import psutil

curDir = os.getcwd()


def is_application_running(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def kill_application(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                proc.terminate()  # 发送终止信号
                proc.wait(timeout=5)  # 等待进程退出
                print(
                    f"Process {proc.info['name']} (PID: {proc.info['pid']}) has been terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            print(f"Failed to terminate process: {e}")


class RealTrader(TraderInf):
    def __init__(self):
        self.app_name = "jy"

    def login(self):
        if is_application_running(self.app_name):
            return
        return os.system(
            f"""osascript {curDir}/trader/autoscpt/real/fy_login.applescript""")

    def balance(self):
        return "real balance"

    def position(self):
        return "real position"

    def buy(self, code, num):
        self.login()
        if is_application_running(self.app_name):
            return os.system(
                f"""osascript {curDir}/trader/autoscpt/real/fy_buy_rr.applescript {code} {num}""")

    def sell(self, code):
        self.login()
        if is_application_running(self.app_name):
            return os.system(
                f"""osascript {curDir}/trader/autoscpt/real/fy_sell_rr.applescript {code} 100""")

    def hold(self):
        self.login()
        if is_application_running(self.app_name):
            result = subprocess.run(
                ['osascript', f"""{curDir}/trader/autoscpt/real/fy_hold_rr.applescript"""], text=True, capture_output=True)
            km_output = result.stdout.strip()
            return km_output


if __name__ == "__main__":
    trader = RealTrader()
    print(trader.hold())
