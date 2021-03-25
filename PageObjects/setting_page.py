"""
-*- coding: utf-8 -*-
File    : setting_page.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.settingpage_locators import SettingPageLocator as loc
from Common.basepage import BasePage

class SettingPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver


    def logout_isExsit(self):

        # 向上滑动
        self.swipe_up()
        try:
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc.logout_text_view))\
            self.wait_eleVisible(loc.logout_text_view)
            return True
        except:
            return False

    def logout(self):
        # 向上滑动
        self.swipe_up()

        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc.logout_text_view))
        self.wait_eleVisible(loc.logout_text_view)
        # self.driver.find_element(*loc.logout_text_view).click()
        self.ele_click(loc.logout_text_view)


