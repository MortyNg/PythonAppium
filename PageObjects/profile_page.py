"""
-*- coding: utf-8 -*-
File    : profile_page.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium import webdriver
from PageLocators.profilepage_locators import ProfilePageLocator as loc
from Common.basepage import BasePage

class ProfilePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def login(self):
        # self.driver.find_element(*loc.my_layout).click()
        self.ele_click(loc.my_layout)

    # 设置
    def setting(self):
        # self.driver.find_element(*loc.setting_layout).click()
        self.ele_click(loc.setting_layout)

    def get_username(self):
        # return self.driver.find_element(*loc.user_name_textview).text
        return self.get_Text()