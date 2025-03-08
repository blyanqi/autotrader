import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

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

    def start_task(self):
        '''启动任务'''
        self.scheduler.start()

    def hello_world(self):
        print("Hello World")
        print(datetime.datetime.now())


if __name__ == '__main__':
    task = Task()
    task.create_task(task.hello_world, 5)
