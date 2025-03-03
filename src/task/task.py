import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


class Task:
    def __init__(self):
        self.currentDir = os.path.dirname(__file__)
        self.scheduler = BlockingScheduler()

    def create_task(self, job, seconds, args=None):
        print(f"Doing starting task {job.__str__()}")
        self.scheduler.add_job(job, 'interval', seconds=seconds, args=args)

    def start_task(self):
        self.scheduler.start()

    def hello_world(self):
        print("Hello World")
        print(datetime.datetime.now())


if __name__ == '__main__':
    task = Task()
    task.create_task(task.hello_world, 5)
