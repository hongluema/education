# -*- coding: utf-8 -*-
from datetime import datetime

import gevent
import requests


def do_somethings(i):
    print "{} start: ".format(i),datetime.now()
    gevent.sleep(0) #让当前的greenlet睡眠N秒,这0标识控制其它协程而不会让其它进程睡眠
    requests.get("http://google.cn")
    print "{} end: ".format(i),datetime.now()

tasks = [gevent.spawn(do_somethings,i) for i in range(3)]
gevent.joinall(tasks)



def foo():
    print('Running in foo')
    gevent.sleep(0) #让当前的greenlet睡眠N秒,这0标识控制其它协程而不会让其它进程睡眠
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([  #gevent.Greenlet实例,直到这个greenlet完成或者超时
    gevent.spawn(foo),  #spawn可以实现一个grennlet实例并且加到队列并且启动,效果类似于gevent.Greenlet(foo).start()
    gevent.spawn(bar),
])

