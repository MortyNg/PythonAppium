"""
-*- coding: utf-8 -*-
File    : welcom_page.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.welcompage_locators import WelcomPageLocator as loc
from Common.basepage import BasePage

class WelcomPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver


    def login_register(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.gotoLoginView))
        self.wait_eleVisible(loc.gotoLoginView)
        # self.driver.find_element(*loc.gotoLoginView).click()
        self.ele_click(loc.gotoLoginView)


    def MainView(self):
        self.wait_eleVisible(loc.gotoMainView)
        # self.driver.find_element(loc.gotoMainView).click()
        self.ele_click(loc.gotoMainView)