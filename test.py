"""
-*- coding: utf-8 -*-
File    : test.py
Version : 0.1
Author  : usrpi
Date    :2021/1/28
"""
# "//*[contains(@text, "+  " "账号不能为空")]"
# a = '//*[contains(@text,'
# b = '"账号不能为空")]'
# print(a + b)
#
#
# # (MobileBy.XPATH, '//*[contains(@text,"账号不能为空")]')
#
# a = "(MobileBy.XPATH, '//*[contains(@text,"
# b = '"账号不能为空"'
# c = ")]')"
# print(a + b +c)
# print("(MobileBy.XPATH, '//*[contains(@text," + '"账号不能为空"' + ")]')")

# loc = "'//*[contains(@text," + '"账号不能为空"' + ")]'"
# print(loc)
import datetime
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

goto_qqlogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_qqlogin')
print(type(goto_qqlogin))

start = datetime.datetime.now()
sleep(2)
end = datetime.datetime.now()
# 求一个差值，写在日志中，就是等待了多久
x = end - start
print(type(x))
print("等待结束，等待时长为：%s" % x)
print(str(x))


t = datetime.datetime.now()
str(t)
print(str(t))