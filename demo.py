"""
-*- coding: utf-8 -*-
File    : demo.py
Version : 0.1
Author  : usrpi
Date    :2020/9/28
"""
from time import sleep

from appium import webdriver

desired_caps = {}
# 平台类型
desired_caps["platformName"] = "Android"
# 平台版本
desired_caps["platformVersion"] = "5.1"
# 设备名称
desired_caps["deviceName"] = "Android Emulator"
# app包名
desired_caps["appPackage"] = "com.nowcoder.app.florida"
# app入口activity
desired_caps["appActivity"] = "com.nowcoder.app.florida.activity.home.SplashActivity"
# app是否重置再打开
desired_caps["noReset"] = "true"

# 连接appium server。 前提：appium desktop要启动，有监听端口
# 要将我们的服务器参数发送过去
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 运行代码之前：1、appium server 启动成功，出于监听状态
# 2、模拟器/真机必须能够被电脑识别。即adb devices能够识别到要操作的设备

# 首次启动，用户隐私协议
sleep(3)
# driver.find_element_by_id('com.nowcoder.app.florida:id/dv_btn_ok').click()
# driver.find_element_by_id('com.nowcoder.app.florida:id/dv_lin_bottom').click()

# 首次启动，用户注册和随便看看
# driver.find_element_by_id('com.nowcoder.app.florida:id/gotoLoginView').click()  # 用户注册登录
driver.find_element_by_id('com.nowcoder.app.florida:id/gotoMainView').click()   # 随便看看

# 关闭登录页面
sleep(5)
# driver.find_element_by_id('com.nowcoder.app.florida:id/back_iv').click()

# 选择密码登录
driver.find_element_by_id('com.nowcoder.app.florida:id/btn_switch_veritype').click()
# 选择海外手机号登录
driver.find_element_by_id('com.nowcoder.app.florida:id/goto_oversea_page').click()
driver.find_element_by_id('com.nowcoder.app.florida:id/country_textview').click()
driver.find_elements_by_id('com.nowcoder.app.florida:id/item_relative')[1].click()

# 登录
sleep(3)
driver.find_element_by_id('com.nowcoder.app.florida:id/loginnumber_phones').send_keys('5678250990')
driver.find_element_by_id('com.nowcoder.app.florida:id/loginnumber_password').send_keys('Aa112211')
driver.find_element_by_id('com.nowcoder.app.florida:id/go_numberlogin').click()
driver.f