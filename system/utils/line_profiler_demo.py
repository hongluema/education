# encoding: utf-8
from line_profiler import LineProfiler
import random

def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i] / 66 for i in range(len(numbers))]
    m = ["hello" + str(numbers[i]) for i in range(len(numbers))]

numbers = random.sample(range(1000),16)

lp = LineProfiler()
lp_wrapper = lp(do_stuff) # 参数是函数do_stuff，分析函数的每一行
lp_wrapper(numbers) #函数do_stuff有参数的话，这里就填参数，没有的话就不填
lp.print_stats()


def do_something():
    a = []
    for i in range(16):
        a.append(i**2)
    print "end"

lp = LineProfiler()
lp_wrapper = lp(do_something) #参数是函数do_something，分析函数的每一行
lp_wrapper() #do_something没有参数，没有的话就不填
lp.print_stats()