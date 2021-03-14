"""
-*- coding: utf-8 -*-
File    : get_toast.py
Version : 0.1
Author  : usrpi
Date    :2021/1/28
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GetToast:

    def __init__(self, driver):
        self.driver = driver

    def get_toast(self, msg):
        try:
            toast_loc = (MobileBy.XPATH, ".//*[contains(@text,'%s')]" %msg)
            WebDriverWait(self.driver, 10, 0.05).until(EC.presence_of_element_located(toast_loc))
            return self.driver.find_element(*toast_loc).text
        except:
            print("没有找到匹配的toast--'%s'！！！" %msg )