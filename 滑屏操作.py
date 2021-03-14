"""
-*- coding: utf-8 -*-
File    : 滑屏操作.py
Version : 0.1
Author  : usrpi
Date    :2020/9/29
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.welcompage_locators import WelcomPageLocator as locwp
from PageLocators.mainpage_locators import MainPageLocators as locmp


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

# 将我们的服务器参数发送出去\

#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, '')))
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# driver.find_element(*locwp.gotoMainView).click()
# driver.find_element(*locmp.tab_job).click()
# sleep(2)
# driver.find_element(*locmp.tab_message).click()
# sleep(2)
# driver.find_element(*locmp.tab_study).click()
sleep(3)
driver.find_element(*locmp.comtab_communitymunity).click()

# 获取屏幕大小 width height
size = driver.get_window_size()
print(size)

start_x = size['width'] * 0.9
start_y = size['height'] * 0.5

end_x = size['width'] * 0.1
end_y = size['height'] * 0.5

# 从右向左滑动 Y轴不变，X轴变小
driver.swipe(start_x, start_y, end_x, end_y, 200)
sleep(2)
# 从左向右滑动 Y轴不变，X轴变大
driver.swipe(end_x, end_y, start_x, start_y, 200)

sleep(2)
# 向上滑动 X轴不变，Y轴变小
driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.1)
sleep(2)
# 向下滑动 X轴不变，Y轴变大
driver.swipe(size['width'] * 0.5, size['height'] * 0.1, size['width'] * 0.5, size['height'] * 0.9)




