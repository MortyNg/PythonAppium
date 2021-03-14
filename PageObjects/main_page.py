"""
-*- coding: utf-8 -*-
File    : main_page.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.mainpage_locators import MainPageLocators as loc
from Common.basepage import BasePage

class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def tab_profile(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.tab_profile))
        self.wait_eleVisible(loc.tab_profile)
        # self.driver.find_element(*loc.tab_profile).click()
        self.ele_click(loc.tab_profile)


