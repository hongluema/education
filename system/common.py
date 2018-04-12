# encoding: utf-8

import functools
import time
import traceback as tb
from system import logger
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from hashlib import sha1
from collections import Counter
import redis
import random
from decimal import Decimal
import string

"""
记录的日志会存放在system目录下的log文件中，因为虽然函数是在app的views文件中,views中的log日志记录的东西都存放在app下的log文件中，
但是装饰器实际上是在system的common文件中执行的，所装饰器里的log记录的日志就是存放在system的log文件中
"""


def wrap(func):
    """
    接口装饰器
    :param func:
    :return:
    """
    @csrf_exempt
    @functools.wraps(func)  # 加上这一句是为了保持原函数名字和属性
    def wrapper(request):
        if request.method == "GET":
            logger.info(
                'func path = {}, method = GET, request params = {}'.format(func.__module__ + '.' + func.__name__,
                                                                           request.GET.dict()))
        elif request.method == "POST":
            logger.info(
                'func path = {}, method = POST, request params = {}'.format(func.__module__ + '.' + func.__name__,
                                                                            request.POST.dict()))
        content = {"status": 200}
        response = HttpResponse(content_type="application/json")  # 默认是传输的json格式
        response["Access-Control-Allow-Origin"] = "*"
        try:
            func(request, response, content)
            if response["Content-Type"] == "application/json":
                response.content = json.dumps(content)
            else:  # 不是返回json的结果
                response.content = content
        except Exception, e:
            logger.exception("")
            tb.print_exc()
            content["status"] = 300
            content["data"] = {"msg": "服务器错误"}
            response.content = json.dumps(content)
        return response


def timestamp(date_time):  # 将datetime时间类型转化为时间戳
    """
    将datetime时间类型转为时间戳
    :param date_time:
    :return:
    """
    time_stamp = int(time.mktime(date_time.timetuple()))
    return time_stamp


def sha1_params(params):
    """
    参数按key值排序
    :param params:
    :return:
    """
    query = ""
    dict_params = {}
    for key, value in params.items():
        dict_params[key] = value
    for key in sorted(dict_params.keys()):  # 把参数按key值排序：这是下单请求的参数格式规定
        query = query + '%s=%s&' % (key, dict_params[key])
    query = query.strip("&")
    query = sha1(query).hexdigest()
    return query


def list_or_str_items_count(list_or_str, most_common=False):
    """
    计算列表或字符串中元素出现的个数, 并可以计算出现次数最多的前most_common个元素
    :param list_or_str:  列表或字符串及其他可迭代的数据
    :param most_common:  int类型，出现次数最多的n个元素
    :return: if most_common: [('a', 3), ('f', 3), ('s', 3), ('e', 2), ('d', 2)]  else: Counter({'a': 3, 'f': 3, 's': 3, 'e': 2, 'd': 2, 'r': 2, 'w': 2, 't': 1})
    """
    c = Counter(list_or_str)
    if most_common:
        c = c.most_common(int(most_common))
    return c


rds = {}


def get_redis(db=0):
    """
    连接redis数据库
    :param db: 数据库的库号
    :return:
    """
    global rds  # 之所以设置全局变量，是为了防止打开多个redis链接，造成并发
    password = "user:password"  # password = user+":"+password
    default = redis.Redis(host="host", port=6379, db=db, password=password)
    return rds.setdefault(db, default)


def rand_str(n):
    """
    用于生成随机字符串
    :param n:  随机字符串的长度
    :return:
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in xrange(n))


def change_money(money):
    """
    转换金额为decimal
    :param money:  金额数，字符串或其他类型
    :return:
    """
    dmoney = Decimal(money).quantize(Decimal('0.00'))
    return dmoney
