"""
-*- coding: utf-8 -*-
File    : toast获取.py
Version : 0.1
Author  : usrpi
Date    :2021/1/14
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocators as loc
from PageLocators.welcompage_locators import WelcomPageLocator as locw
"""
要获取toast信息要满足以下两个要求：
1.appium server版本1.6.3+才支持toast获取(而appium server 1.6.3没有可视化界面，解决方案：下载appium-desktop-Setup-1.4.1
ia32.exe)
2.代码中必须指定automationName为：UIAutomator2
3.UIAutomator2只支持安卓版本5.0+
因此，因为他们的最高支持安卓版本为4.4.2,可以使用genymotion模拟器
4、要求安装jdk1.8 64位及以上，配置其环境变量JAVA_HOME和path
"""

desired_caps = {}
desired_caps["automationName"] = "UIAutomator2"
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

# self.lp = LoginPage(self.driver)
# 运行代码之前：1、appium server 启动成功，出于监听状态
# 2、模拟器/真机必须能够被电脑识别。即adb devices能够识别到要操作的设备

sleep(3)
driver.find_element(*locw.gotoLoginView).click()
sleep(3)
# 点击密码登录
driver.find_element(*loc.btn_switch_veritype).click()
# 选择海外手机号登录
driver.find_element(*loc.goto_oversea_page).click()

# 选择区号
driver.find_element(*loc.country_textview).click()
sleep(3)
# 选择美国
driver.find_elements(*loc.item_relative)[1].click()
sleep(3)
# 输入手机号
driver.find_element(*loc.loginnumber_phones).send_keys('')
# 输入密码
driver.find_element(*loc.loginnumber_password).send_keys('')
# 登录
driver.find_element(*loc.go_numberlogin).click()

loc = (MobileBy.XPATH, '//*[contains(@text,"账号不能为空")]')
# check = '账号不能为空'

# 等待的时候，要用元素存在的条件，不能用元素可见的条件
# try:
#     WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located(loc))
#     print(driver.find_element(*loc).text)
#
# except:
#     print('没有找到匹配的toast！！！')

def get_toast(check):
    try:
        toast_loc = (MobileBy.XPATH, ".//*[contains(@text,'%s')]" % check)
        WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located(toast_loc))
        print(toast_loc)
        print(driver.find_element(*toast_loc).text)
    except:
        print("没有找到匹配的toast--'s%'！！！" )
        print(toast_loc)


print(get_toast('账号不能为空'))

