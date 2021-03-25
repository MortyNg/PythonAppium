"""
-*- coding: utf-8 -*-
File    : basepage.py
Version : 0.1
Author  : usrpi
Date    :2021/1/29
"""

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime
from Common import dir_config
from Common import logger
# 封装基本函数 -- 执行日志、处理异常、失败截图
# 所有的页面公共部分，不涉及业务

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 元素等待可见
    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc= ""):
        """
        :param locator: 元素定位。元组形式。（元素定位类型、元素定位方式）
        :param wait_times: 等待时间
        :param poll_frequency: 轮询时间
        :param doc: 模块名_页面名称_操作名称
        :return: None
        """
        logging.info("等待元素: %s,%s" % locator) # locator是一个元组，有两个数据，所以需要%s,%s两个一一对应，才不会报错
        # logging.info('等待元素: {0}'.format(locator))
        try:
            # 开始等待时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，就是等待了多久
            wait = (end - start).seconds
            logging.info("等待结束，等待时长为：%s" % wait)
        except:
            # 捕获异常到日志中
            logging.exception('等待 %s,%s 元素可见失败！！！' % locator)
            # 抛出异常
            raise

    # 查找元素
    def get_ele(self, locator, doc= ""):
        logging.info('查找元素：%s,%s' % locator)
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败：%s,%s' % locator)
            raise

    def get_eles(self, locator, doc= ""):
        logging.info('查找符合表达式的所有元素：%s,%s' % locator)
        try:
            return self.driver.find_elements(*locator)
        except:
            logging.exception('查找元素失败：%s,%s' % locator)
            raise

    # 元素点击操作
    def ele_click(self, locator, doc= ""):
        # 找元素
        ele = self.get_ele(locator)
        # 元素点击操作
        logging.info('点击元素：%s,%s' % locator)
        try:
            ele.click()
        except:
            logging.exception('元素点击操作失败：%s,%s' % locator)
            raise

    # 元素点击操作
    def eles_click(self, locator, num, doc= ""):

        logging.info('点击元素：%s,%s' % locator)
        try:
            self.driver.find_elements(*locator)[num].click()
        except:
            logging.exception('元素点击操作失败：%s,%s' % locator)
            raise

     # 元素输入操作
    def text_input(self, locator, text, doc= ""):
        # 找元素
        ele = self.get_ele(locator)
        # 元素输入操作
        logging.info('输入数据：%s' % text)
        try:
            ele.send_keys(text)
        except:
            logging.exception('数据输入操作失败：%s' % text)
            raise

    # 获取元素文本
    def get_Text(self, locator, doc= ""):
        # 找元素
        ele = self.get_ele(locator)
        try:
            return ele.text
        except:
            logging.exception('获取 %s,%s 元素的文本失败！！' % locator)
            raise

    # 获取元素属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_ele(locator, doc)
        logging.info('%s：获取元素：%s的属性：%s' %doc,locator,attr)
        try:
            ele_attr = ele.get_attribute(attr)
            logging.info('元素：%s的属性%s值为：%s' %locator, attr, ele_attr)
            return ele_attr
        except:
            logging.exception('获取元素的属性失败！！！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 元素是否存在，存在则为True，否则为False
    def is_eleExist(self, locator, timeout=10, doc=""):
        logging.info('在页面 %s 中是否存在元素：%s' % doc, locator)
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info('%s 秒内页面 %s 中存在元素：%s' % timeout, doc, locator)
            return True
        except:
            logging.info('%s 秒内页面 %s 中不存在元素：%s' % timeout, doc, locator)
            return False

    # 获取整个屏幕大小
    def get_screensize(self):
        return self.driver.get_window_size()

    # 向上滑动
    def swipe_up(self):
        # 获取整个屏幕大小 width height
        size = self.get_screensize()
        # 向上滑动 X轴不变，Y轴变小
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)

    # 向下滑动
    def swipe_down(self):
        # 获取屏幕大小 width height
        size = self.driver.get_window_size()
        # 向下滑动 X轴不变，Y轴变大
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.1, size['width'] * 0.5, size['height'] * 0.9)

    # 向左滑动
    def swipe_left(self):
        # 获取屏幕大小 width height
        size = self.get_screensize()

        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.5

        end_x = size['width'] * 0.1
        end_y = size['height'] * 0.5

        # 从右向左滑动 Y轴不变，X轴变小
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    # 向右滑动
    def swipe_right(self):
        # 获取屏幕大小 width height
        size = self.get_screensize()

        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.5

        end_x = size['width'] * 0.1
        end_y = size['height'] * 0.5

        # 从左向右滑动 Y轴不变，X轴变大
        self.driver.swipe(end_x, end_y, start_x, start_y, 200)

    # toast获取
    def get_toast(self, msg):
        try:
            toast_loc = (MobileBy.XPATH, ".//*[contains(@text,'%s')]" % msg)
            WebDriverWait(self.driver, 10, 0.05).until(EC.presence_of_element_located(toast_loc))
            return self.driver.find_element(*toast_loc).text
            # return self.get_text(*toast_loc) # 调用get_text无法获取toast ？？？
        except:
            logging.exception("没有找到匹配的toast--'%s'！！！" % msg )
            raise

    # H5切换
    # 截屏操作
    # def save_screenshot(self, doc):
    #     # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
    #     # filepath 指的图片保存目录/model（页面功能名称）_当前时间到秒.png
    #     filePath = dir_config.screenshot_dir + \ '/%s_%s.png' % doc, time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    #     # 截图文件存放在 Screenshot 目录下
    #     # driver方法：self.driver.save_screenshot()
    #     try:
    #         self.driver.save_screenshot(filePath)
    #         logging.info('截屏成功，图片路径为 %s' % filePath)
    #     except:
    #         logging.exception('截屏失败！！！')
