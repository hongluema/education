# encoding: utf-8

from celery import Celery
import time

broker = 'redis://127.0.0.1:6379'  # 消息中间件，任务调度队列
backend = 'redis://127.0.0.1:6379/0'  # 任务结果存储

app = Celery("my_task", broker=broker, backend=backend)

@app.task
def add(x,y):
    time.sleep(6) #模拟耗时操作
    return x+y
"""
上面的代码做了几件事：
    创建了一个Celery实例app，名称为my_task；
    指定消息中间件用redis，URL为redis://127.0.0.1:6379；
    指定存储用redis，URL为redis://127.0.0.1:6379/0；
    创建了一个Celey任务add，当函数被@app.task装饰后，就成为可被Celery调度的任务；
"""
