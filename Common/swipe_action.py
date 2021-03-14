"""
-*- coding: utf-8 -*-
File    : swipe_action.py
Version : 0.1
Author  : usrpi
Date    :2021/1/29
"""

class SwipeAction:
    def __init__(self, driver):
        self.driver = driver

    def swipe_lelf(self):
        # 获取屏幕大小 width height
        size = self.driver.get_window_size()
        print(size)

        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.5

        end_x = size['width'] * 0.1
        end_y = size['height'] * 0.5

        # 从右向左滑动 Y轴不变，X轴变小
        self.driver.swipe(start_x, start_y, end_x, end_y, 200)

    def swipe_right(self):
        # 获取屏幕大小 width height
        size = self.driver.get_window_size()

        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.5

        end_x = size['width'] * 0.1
        end_y = size['height'] * 0.5

        # 从左向右滑动 Y轴不变，X轴变大
        self.driver.swipe(end_x, end_y, start_x, start_y, 200)

    def swipe_up(self):
        # 获取屏幕大小 width height
        size = self.driver.get_window_size()
        # 向上滑动 X轴不变，Y轴变小
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)

    def swipe_down(self):
        # 获取屏幕大小 width height
        size = self.driver.get_window_size()
        # 向下滑动 X轴不变，Y轴变大
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.1, size['width'] * 0.5, size['height'] * 0.9)

