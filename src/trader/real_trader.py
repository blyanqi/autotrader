import logging
import os
import subprocess
from src.core.logger import Logger
from src.trader.trader_inf import TraderInf
import psutil


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
        self.logger = Logger.get_logger("real_trader")
        self.curDir = os.path.dirname(__file__)
        self.scriptDir = os.path.join(
            self.curDir, "autoscpt", "real")
        self.login()

    def login(self):
        try:
            if is_application_running(self.app_name):
                self.logger.info("already login")
                return True
            loginStatus = os.system(
                f"""osascript {self.scriptDir}/fy_login.applescript""")
            self.logger.info(f"loginStatus: {loginStatus}")
            return loginStatus
        except Exception as e:
            self.logger.error(f"login error: {e}")
            return False

    def balance(self):
        try:
            self.login()
            if is_application_running(self.app_name):
                self.logger.info(
                    f"""{self.scriptDir}/fy_balance_rr.applescript""")
                result = subprocess.run(
                    ['osascript', f"""{self.scriptDir}/fy_balance_rr.applescript"""], text=True, capture_output=True)
                km_output = result.stdout.strip()
                return km_output
        except Exception as e:
            self.logger.error(f"buy error: {e}")
            return False

    def position(self):
        return "real position"

    def buy(self, code, num):
        try:
            if not self.login():
                self.logger.info("login failed")
                return
            if is_application_running(self.app_name):
                return os.system(
                    f"""osascript {self.scriptDir}/fy_buy_rr.applescript {code} {num}""")
        except Exception as e:
            self.logger.error(f"buy error: {e}")
            return False

    def sell_all(self, code):
        try:
            if not self.login():
                self.logger.info("login failed")
                return
            if is_application_running(self.app_name):
                return os.system(
                    f"""osascript {self.scriptDir}/fy_sell_all_rr.applescript {code}""")
        except Exception as e:
            self.logger.error(f"sell_all error: {e}")

    def sell(self, code, num):
        try:
            if not self.login():
                self.logger.info("login failed")
                return
            if is_application_running(self.app_name):
                return os.system(
                    f"""osascript {self.scriptDir}/fy_sell_rr.applescript {code} {num}""")
        except Exception as e:
            self.logger.error(f"sell error: {e}")
            return False

    def hold(self):
        try:
            if not self.login():
                self.logger.info("login failed")
                return
            if is_application_running(self.app_name):
                self.logger.info(
                    f"""{self.scriptDir}/fy_hold_rr.applescript""")
                result = subprocess.run(
                    ['osascript', f"""{self.scriptDir}/fy_hold_rr.applescript"""], text=True, capture_output=True)
                km_output = result.stdout.strip()
                return km_output
        except Exception as e:
            self.logger.error(f"sell error: {e}")
            return ""


if __name__ == "__main__":
    trader = RealTrader()
    print(trader.hold())
