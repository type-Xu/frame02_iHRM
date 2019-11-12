"""
    框架搭建:
        核心: api + case + data
            |-- api: 封装请求业务(requests)
            |-- case: 集成 unittest 实现, 调用 api 以及参数化解析 data
            |-- data: 封装测试数据
        报告: report + tools + run_suite.py
            |-- report: 保存测试报告
            |-- tools: 封装工具文件
            |-- run_suite.py: 组织测试套件
        配置: app.py
            |-- app.py：封装程序常量以及配置信息
        日志: log
            |-- log: 保存日志文件
"""
import logging
import os
import logging.handlers

# 封装接口的 URL 前缀

BASE_URL = "http://182.92.81.159"

# 封装项目路径
FILE_PATH = os.path.abspath(__file__)
PRO_PATH = os.path.dirname(FILE_PATH)

# 代码简化 -- 变体
# PRO_PATH1 = os.path.dirname(os.path.abspath(__file__))
# PRO_PATH2 = os.getcwd()
# print("动态获取的项目绝对路径:",PRO_PATH)
# print("动态获取的项目绝对路径:",PRO_PATH1)
# print("动态获取的项目绝对路径:",PRO_PATH2)

# 定义一个变量
TOKEN = None
USER_ID = None


# 日志模块实现
def my_log_config():
    # 获取日志对象
    logger = logging.getLogger()
    # 配置输出级别info以上
    logger.setLevel(logging.INFO)
    # 配置输出目标,控制台和磁盘文件
    cv = logging.StreamHandler()
    cv02 = logging.handlers.TimedRotatingFileHandler(PRO_PATH + "/log/mylog.log",
                                                     when="h",
                                                     interval=12,
                                                     backupCount=14,
                                                     encoding="utf-8")
    # 配置输出格式__年月日时分秒 用户 级别 python文件 函数
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 组织配置并添加日志对象
    cv.setFormatter(formatter)
    cv02.setFormatter(formatter)
    logger.addHandler(cv)
    logger.addHandler(cv02)

    # 调用,在需要的位置调用日志输出
#     实现:
# 步骤1:报下的__init__,py初始化日志配置
        # import app
        # app.my_log_config()
# 步骤2:报下的__init__,py初始化日志配置

# my_log_config()
# logging.info("hello")
# logging.warning("危险")
