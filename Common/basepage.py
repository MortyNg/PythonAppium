"""
-*- coding: utf-8 -*-
File    : basepage.py
Version : 0.1
Author  : usrpi
Date    :2021/1/29
"""
import time
from logging import handlers

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import datetime
# 封装基本函数 -- 执行日志、处理异常、失败截图
# 所有的页面公共部分，不涉及业务

class BasePage:
    logger = logging.getLogger()  # 不加名称设置root logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    t = time.time()
    # t = datetime.datetime.now()


    # 使用FileHandler输出到文件
    fh = logging.FileHandler('../Outputs/'+ str(t) +'.log') # 设置log路径和文件名
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)

    # 使用StreamHandler输出到屏幕
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    # 添加两个Handler
    logger.addHandler(ch)
    logger.addHandler(fh)
    # # 默认WARNING级别的日志才会在控制台输出，故需要重新设置为INFO级别
    # t = time.time()
    # logging.basicConfig(level=logging.INFO,
    #                     filename=str(t) +'.log',
    #                     filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    #                     # a是追加模式，默认如果不写的话，就是追加模式
    #                     format=
    #                     '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    #                     # 日志格式
    #                     )

    def __init__(self, driver):
        self.driver = driver

    # 元素等待
    def wait_eleVisible(self, loc):
        logging.info("等待元素: %s,%s" % loc) # loc是一个元组，有两个数据，所以需要%s,%s两个一一对应，才不会报错
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，就是等待了多久
            logging.info("等待结束，等待时长为：%s" % (end - start))
        except:
            logging.exception('等待 %s,%s 元素可见失败！！！' % loc)
            raise

    # 查找元素
    def get_ele(self, loc):
        logging.info('查找元素：%s,%s' % loc)
        try:
            return self.driver.find_element(*loc)
        except:
            logging.exception('查找元素失败：%s,%s' % loc)
            raise

    # 元素点击操作
    def ele_click(self, loc):
        # 找元素
        ele = self.get_ele(loc)
        # 元素点击操作
        logging.info('点击元素：%s,%s' % loc)
        try:
            ele.click()
        except:
            logging.exception('元素点击操作失败：%s,%s' % loc)
            raise

    # 元素点击操作
    def eles_click(self, loc, num):

        logging.info('点击元素：%s,%s' % loc)
        try:
            self.driver.find_elements(*loc)[num].click()
        except:
            logging.exception('元素点击操作失败：%s,%s' % loc)
            raise

     # 元素输入操作
    def text_input(self, loc, text):
        # 找元素
        ele = self.get_ele(loc)
        # 元素输入操作
        logging.info('输入数据：%s' % text)
        try:
            ele.send_keys(text)
        except:
            logging.exception('数据输入操作失败：%s' % text)
            raise

    # 获取元素文本
    def get_Text(self, loc):
        # 找元素
        ele = self.get_ele(loc)
        try:
            return ele.text
        except:
            logging.exception('获取 %s,%s 元素的文本失败！！' % loc)
            raise

