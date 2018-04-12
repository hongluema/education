# encoding: utf-8
import logging
import os

logger = logging.getLogger(__name__)  # 因为在模块中，__name__是Python包含命名空间中的模块名称
logger.level = logging.INFO
formatter = logging.Formatter(
    '%(name)s %(levelname)s %(module)s %(funcName)s %(lineno)d %(asctime)s %(message)s')  # 实例使用消息的整个格式字符串以及消息的日期/时间部分的格式字符串进行初始化
handler = logging.FileHandler(
    filename=os.path.dirname(__file__) + "/log")  # 指的是当前文件所在的目录，放在log日志里面就是哪里引用log日志，就会在那个文件的目录下创建log文件
handler.setFormatter(formatter)  # 设置日志文件格式
logger.addHandler(handler)  # 将指定的处理程序handler添加到此记录器
# os.path.dirname(__file__) 指的是当前文件所在的目录，放在log日志里面就是哪里引用log日志，就会在那个文件的目录下创建log文件
