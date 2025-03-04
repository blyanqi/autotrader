import datetime


class Policy():
    def __init__(self, filter):
        self.filter = filter
        self.policy = {
            "rate_turnover": {
                "name": "rate_turnover",
                "desc": "首先过滤出前一天涨停的个股。然后根据换手率过滤，涨幅在一定区间类的个股。依据是高换手意味着人气高。"
            },
            "rate_turnover_curday": {
                "name": "rate_turnover_curday",
                "desc": "根据换手率过滤，涨幅在一定区间类的个股。依据是高换手意味着人气高。"
            }
        }
        self.time_zone = {
            "first": {
                "start": datetime.time(9, 25),
                "end": datetime.time(9, 35),
                "turnover": 5,
                "min_rate": 2,
                "max_rate": 5,
            },
            "second": {
                "start": datetime.time(9, 36),
                "end": datetime.time(9, 45),
                "turnover": 10,
                "min_rate": 2,
                "max_rate": 5,
            },
            "third": {
                "start": datetime.time(9, 46),
                "end": datetime.time(10, 00),
                "turnover": 12,
                "min_rate": 2,
                "max_rate": 5,
            },
            "other": {
                "turnover": 20,
                "min_rate": 2,
                "max_rate": 5,
            }
        }

    def get_time(self):
        time = datetime.datetime.now().time()
        return time

    def get_today(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        return today

    def top_rate_turnover_policy(self):
        '''有过涨停的股票'''
        # 时间在 9:25-9:35、9:35-9:45、9:45-10:00之间
        filename = self.policy["rate_turnover"]["name"] + self.get_today()
        if self.get_time() <= self.time_zone["first"]["end"]:
            filename += "_"+self.time_zone["first"]["end"].strftime("%H:%M")
            self.filter.filter_top_with_rate_turnover(
                self.time_zone["first"]["min_rate"], self.time_zone["first"]["max_rate"],
                self.time_zone["first"]["turnover"], filename)
            return
        if self.get_time() <= self.time_zone["second"]["end"]:
            filename += "_"+self.time_zone["second"]["end"].strftime("%H:%M")
            self.filter.filter_top_with_rate_turnover(
                self.time_zone["second"]["min_rate"], self.time_zone["second"]["max_rate"],
                self.time_zone["second"]["turnover"], filename)
            return
        if self.get_time() <= self.time_zone["third"]["end"]:
            filename += "_"+self.time_zone["third"]["end"].strftime("%H:%M")
            self.filter.filter_top_with_rate_turnover(
                self.time_zone["third"]["min_rate"], self.time_zone["third"]["max_rate"],
                self.time_zone["third"]["turnover"], filename)
        else:
            filename += "_"+"other"
            self.filter.filter_top_with_rate_turnover(
                self.time_zone["other"]["min_rate"], self.time_zone["other"]["max_rate"],
                self.time_zone["other"]["turnover"], filename)

    def top_rate_turnover_policy_day(self):
        '''今日开盘的股票'''
        filename = self.policy["rate_turnover_curday"]["name"] + \
            self.get_today()
        if self.get_time() <= self.time_zone["first"]["end"]:
            filename += "_"+self.time_zone["first"]["end"].strftime("%H:%M")
            self.filter.filter_with_turnover(
                self.time_zone["first"]["min_rate"], self.time_zone["first"]["max_rate"],
                self.time_zone["first"]["turnover"], filename)
            return
        if self.get_time() <= self.time_zone["second"]["end"]:
            filename += "_"+self.time_zone["second"]["end"].strftime("%H:%M")
            self.filter.filter_with_turnover(
                self.time_zone["second"]["min_rate"], self.time_zone["second"]["max_rate"],
                self.time_zone["second"]["turnover"], filename)
            return
        if self.get_time() <= self.time_zone["third"]["end"]:
            filename += "_"+self.time_zone["third"]["end"].strftime("%H:%M")
            self.filter.filter_with_turnover(
                self.time_zone["third"]["min_rate"], self.time_zone["third"]["max_rate"],
                self.time_zone["third"]["turnover"], filename)
        else:
            filename += "_"+"other"
            self.filter.filter_with_turnover(
                self.time_zone["other"]["min_rate"], self.time_zone["other"]["max_rate"],
                self.time_zone["other"]["turnover"], filename)


if __name__ == "__main__":
    policy = Policy(None, None)
    print(policy.top_rate_turnover_policy())
