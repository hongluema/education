# -*- coding: utf-8 -*-

BROKER_URL = "redis://127.0.0.1:6379"                  #指定Broker
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"     #指定Backend
CELERY_TIMEZONE = "Asia/Shanghai"                      #指定时区，默认是UTC
CELERY_IMPORTS = (                                     #指定导入的任务模块
    "celery_app.task1",
    "celery_app.task2"
)

"""
消息中间件 Broker
Broker ，即为任务调度队列，接收任务生产者发来的消息（即任务），将任务存入队列。 Celery 本身不提供队列服务，官方推荐使用 RabbitMQ 和 Redis 等。

任务执行单元 Worker
Worker 是执行任务的处理单元，它实时监控消息队列，获取队列中调度的任务，并执行它。

任务结果存储 Backend
Backend 用于存储任务的执行结果，以供查询。同消息中间件一样，存储也可使用 RabbitMQ, Redis 和 MongoDB 等。
"""