"""
-*- coding: utf-8 -*-
File    : logger.py
Version : 0.1
Author  : usrpi
Date    :2021/3/25
"""
import time
import logging
from logging.handlers import RotatingFileHandler
from Common import dir_config

fmt = '%(asctime)s %(levelname)s %(filename)s %(funcName)s [line:%(lineno)d] %(message)s'
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime('%Y-%m-%d %H%M', time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir+'App_Autotest_%s.log' % curTime, backupCount=20, encoding='utf-8')

# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

logging.info('测试日志文件输出')