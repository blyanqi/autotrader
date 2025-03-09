import datetime

import pandas as pd

from src.core.logger import Logger
from src.core.container import IoCContainer


class Policy():
    def __init__(self, filter):
        container = IoCContainer()
        self.config = container.resolve(
            "config", "")
        self.filter = filter
        self.logger = Logger.get_logger("policy")
        # self.filterMethod = self.filter.filter_with_volumerate
        self.filterMethod = self.filter.filter_with_volumerate_of_before_day

    def str_to_time(self, timeStr):
        return datetime.datetime.strptime(timeStr, "%H:%M").time()

    def get_time(self):
        time = datetime.datetime.now().time()
        return time

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def policy_0(self):
        first = self.config.get_nested_value("policy.0.time_zone.0")
        second = self.config.get_nested_value("policy.0.time_zone.1")
        third = self.config.get_nested_value("policy.0.time_zone.2")
        other = self.config.get_nested_value("policy.0.time_zone.3")

        return {
            "first": {
                "start": self.str_to_time(first["start"]),
                "end": self.str_to_time(first["end"]),
                "volumerate": first["volumerate"],
                "turnover": first["turnover"],
                "min_rate": first["min_rate"],
                "max_rate": first["max_rate"],
                "day60rate": first["day60rate"]
            },
            "second": {
                "start": self.str_to_time(second["start"]),
                "end": self.str_to_time(second["end"]),
                "volumerate": second["volumerate"],
                "turnover": second["turnover"],
                "min_rate": second["min_rate"],
                "max_rate": second["max_rate"],
                "day60rate": second["day60rate"]
            },
            "third": {
                "start": self.str_to_time(third["start"]),
                "end": self.str_to_time(third["end"]),
                "volumerate": third["volumerate"],
                "turnover": third["turnover"],
                "min_rate": third["min_rate"],
                "max_rate": third["max_rate"],
                "day60rate": third["day60rate"]
            },
            "other": {
                "volumerate": other["volumerate"],
                "turnover": other["turnover"],
                "min_rate": other["min_rate"],
                "max_rate": other["max_rate"],
                "day60rate": other["day60rate"]
            }
        }

    def top_volumerate_day(self):
        self.logger.info(f"use policy top_volumerate_day \
            {self.get_time()}")
        p = self.policy_0()
        self.logger.debug(p)
        filename = self.config.get_nested_value(
            "policy.0")["name"] + self.get_today()
        if self.get_time() <= p["first"]["end"]:
            filename += "_"+p["first"]["end"].strftime("%H:%M")
            self.logger.info(f'''min: {p["first"]["min_rate"]}''')
            self.logger.info(f'''max: {p["first"]["max_rate"]}''')
            self.logger.info(f'''volumerate: {p["first"]["volumerate"]}''')
            self.logger.info(f'''day60rate: {p["first"]["day60rate"]}''')
            self.logger.info(f'''filename: {filename}''')
            self.filterMethod(p["first"]["min_rate"],
                              p["first"]["max_rate"],
                              p["first"]["volumerate"],
                              p["first"]["day60rate"],
                              filename)
            return
        if self.get_time() <= p["second"]["end"]:
            filename += "_"+p["second"]["end"].strftime("%H:%M")

            self.filterMethod(p["second"]["min_rate"],
                              p["second"]["max_rate"],
                              p["second"]["volumerate"],
                              p["second"]["day60rate"],
                              filename)
            return
        if self.get_time() <= p["third"]["end"]:
            filename += "_"+p["third"]["end"].strftime("%H:%M")
            self.filterMethod(p["third"]["min_rate"],
                              p["third"]["max_rate"],
                              p["third"]["volumerate"],
                              p["third"]["day60rate"],
                              filename)
        else:
            filename += "_"+"other"
            self.filterMethod(p["other"]["min_rate"],
                              p["other"]["max_rate"],
                              p["other"]["volumerate"],
                              p["other"]["day60rate"],
                              filename)


if __name__ == "__main__":
    policy = Policy(None, None)
    print(policy.top_rate_turnover_policy())
