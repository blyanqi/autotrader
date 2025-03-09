import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from src.core.logger import Logger
from src.entity.task_entity import JobEntity


class Task:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)
        self.scheduler = BlockingScheduler()
        self.logger = Logger.get_logger("task")

    def create_task(self, job: JobEntity):
        '''创建任务'''
        self.logger.info(f"Doing starting task {job.name}...")
        self.scheduler.add_job(
            job.job, 'interval', seconds=job.seconds, args=job.args)

    def create_task_with_cron(self, job: JobEntity):
        '''创建任务
        CronTrigger 的参数如下：
            year (int|str) - 年份（4位数字）
            month (int|str) - 月份（1-12）
            day (int|str) - 月份中的日子（1-31）
            week (int|str) - 星期中的日子（0-6，星期天为0或7）
            day_of_week (int|str) - 星期的日子（0-6，星期天为0或7），可以指定多个值，例如 'mon-fri'
            hour (int|str) - 小时（0-23）
            minute (int|str) - 分钟（0-59）
            second (int|str) - 秒（0-59）
        '''
        f = job.cron.split(" ")
        if len(f) != 6:
            self.logger.error(
                f"cron {job.cron} is not valid, cron format is 'second minute hour day month week'")
            return
        self.logger.info(f"cron: {job.cron}")
        cronTrigger = CronTrigger(second=f[0], minute=f[1],
                                  hour=f[2], day=f[3], week=f[4], month=f[5])
        self.logger.info(f"Doing starting task {job.name}...")
        self.scheduler.add_job(
            job.job, trigger=cronTrigger, args=job.args)

    def start_task(self):
        '''启动任务'''
        self.scheduler.start()

    def hello_world(self):
        print("Hello World")
        print(datetime.datetime.now())


if __name__ == '__main__':
    task = Task()
    task.create_task(task.hello_world, 5)
