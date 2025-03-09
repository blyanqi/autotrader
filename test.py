import os
import pandas as pd
from io import StringIO

from src.entity.task_entity import JobCronEntity, JobEntity
from src.seek.seek_akshare import Seek
from src.task.task import Task

curDir = os.path.dirname(__file__)
job4 = JobCronEntity()
seek = Seek()
task = Task()
job4.name = "snapshot_real_data_10:33"
job4.job = seek.snapshot_real_data
job4.cron = "0 33 10 * * *"
job4.args = ["10:33"]
task.create_task_with_cron(job4)
task.start_task()
