# -*- coding: utf-8 -*-

from celery_app import task1
from celery_app import task2

task1.add.apply_async(args=[2, 8])  # 也可以用 task1.add.delay(2,8)
task2.multiply.apply_async(args=[3, 7])  # 也可以用 task2.multipy.delay(3,7)

print "hello world"
