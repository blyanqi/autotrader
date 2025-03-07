import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import logging


class Task:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)
        self.scheduler = BlockingScheduler()
        self.logger = logging.getLogger(__name__)

    def create_task(self, job, seconds, args=None):
        '''创建任务'''
        self.logger.info(f"Doing starting task ...")
        self.scheduler.add_job(job, 'interval', seconds=seconds, args=args)

    def start_task(self):
        '''启动任务'''
        self.scheduler.start()

    def hello_world(self):
        print("Hello World")
        print(datetime.datetime.now())


if __name__ == '__main__':
    task = Task()
    task.create_task(task.hello_world, 5)
