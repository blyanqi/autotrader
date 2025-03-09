import os
from src.core.container import IoCContainer
import src.core.service as service
from watchdog.observers import Observer
from src.entity.task_entity import JobCronEntity, JobEntity

curDir = os.path.dirname(__file__)
container = IoCContainer()
config = container.resolve("config", f"{curDir}/src/config/config.yaml")
event_handler = container.resolve("configReload", config)
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)
observer.start()


def create_cron_task(seek, task, timeList):
    for item in timeList:
        job = JobCronEntity()
        job.name = "snapshot_real_data_" + item["timer"]
        job.job = seek.snapshot_real_data
        t = item["timer"].split(":")
        job.cron = f"0 {t[1]} {t[0]} * * *"
        job.args = [item["timer"]]
        task.create_task_with_cron(job)


def rate_volumnrate_policy_day(isTrader=False):
    type1 = config.get_nested_value("policy.0")
    task = container.resolve("task")
    seek = container.resolve("seek")
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    filter = container.resolve("filter")
    policy = container.resolve("policy", filter)

    job1 = JobEntity()
    job1.name = config.get("task.real_data.name")
    job1.job = seek.real_data
    job1.seconds = config.get("task.real_data.timer")
    job2 = JobEntity()
    job2.name = config.get("task.policy_top.name")
    job2.job = policy.top_volumerate_day
    job2.seconds = config.get("task.policy_top.timer")
    job3 = JobEntity()
    job3.name = config.get("task.trader.name")
    job3.job = traderExec.policy_buy_stock
    job3.seconds = config.get("task.trader.timer")
    job3.args = [type1["name"]]

    timeList = config.get("task.cron")

    task.create_task(job1)
    task.create_task(job2)
    if isTrader:
        task.create_task(job3)
    create_cron_task(seek, task, timeList)

    task.start_task()


def test_trader():
    trader = container.resolve("realTrader")
    traderExec = container.resolve("traderExec", trader)
    traderExec.sell_all()


if __name__ == '__main__':
    rate_volumnrate_policy_day(True)
    # test_trader()
    pass
