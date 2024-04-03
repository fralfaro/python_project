# -*- coding: utf-8 -*-
from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Celery

graph_attr = {"bgcolor": "transparent"}

with Diagram("Servicio Web de Slotting", show=False, graph_attr=graph_attr):
    with Cluster("Slotting Service"):
        with Cluster("FastAPI Services"):
            service = [
                Python("solve"),
                Python("metrics"),
                Python("task_status"),
                Python("..."),
            ]

        with Cluster("Queue"):
            queue = Redis("Task Queue")

        with Cluster("Workers"):
            workers = [
                Celery("worker_1"),
                Celery("worker_2"),
                Celery("..."),
                Celery("worker_n"),
            ]

        service >> queue >> workers
