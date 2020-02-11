#!/usr/bin/env python
# coding=utf-8

import logging
import os
import datetime
import logging.config
# ****  日志配置  ****
from config.VarConfig import parentDirPath

#通过创建一个包含配置信息的dict，然后把它传递个dictConfig()函数，来配置logging
'''
Python 3.2中引入的一种新的配置日志记录的方法--用字典来保存logging配置信息。
我们可把很多的数据转换成字典。比如，我们可以使用JSON格式的配置文件、YAML格式的配置文件，然后将它们填充到一个配置字典中；或者，我们也可以用Python代码构建这个配置字典，
或者通过socket接收pickled序列化后的配置信息。
总之，你可以使用你的应用程序可以操作的任何方法来构建这个配置字典。
'''

LOG_PATH = os.path.join(parentDirPath, "logs")
LOG_SETTINGS = dict(
    #version是必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1
    version=1,
    #这是一个布尔型值，默认值为True（为了向后兼容）表示禁用已经存在的logger，除非它们或者它们的祖先明确的出现在日志配置中；
    # 如果值为False则对已存在的loggers保持启动状态。
    disable_existing_loggers=False,
    #Formatter 格式化器，指明了最终输出中日志的格式。
    formatters={
        'standard': {
            'format': '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s'
        },
    },
    #Handler 处理器，将日志记录发送至合适的路径。
    handlers={
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH,
                                     "result_{}.log".format(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    #配置logger信息。必须包含一个名字叫做root的logger，当使用无参函数logging.getLogger()时，默认返回root这个
    root={
        'handlers': ['console', 'file'],
        'level': logging.DEBUG,
    },
    #Logger 记录器，用于设置日志采集
    loggers={
        'default': {
            'handlers': ['file', 'console'],
            'level': logging.DEBUG,
            'propagate': False
        },
    }
)

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


def init_log():
    logging.config.dictConfig(LOG_SETTINGS)


if __name__ == "__main__":
    init_log()
    logging.debug("测试一个debug的log")
    logging.info("测试一个info的log")
