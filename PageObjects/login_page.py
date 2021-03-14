"""
-*- coding: utf-8 -*-
File    : login_page.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginPageLocators as loc
from Common.basepage import BasePage

class LoginPage(BasePage):
    # 继承BasePage类后，不在需要初始化函数
    # def __init__(self, driver):
    #     self.driver = driver

    def select_login(self):
        # 点击密码登录
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.btn_switch_veritype))
        self.wait_eleVisible(loc.btn_switch_veritype)
        # self.driver.find_element(*loc.btn_switch_veritype).click()
        self.ele_click(loc.btn_switch_veritype)
        # 选择海外手机号登录
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.goto_oversea_page))
        self.wait_eleVisible(loc.goto_oversea_page)
        # self.driver.find_element(*loc.goto_oversea_page).click()
        self.ele_click(loc.goto_oversea_page)
        # 点击区号
        # self.driver.find_element(*loc.country_textview).click()
        self.ele_click(loc.country_textview)
        # 选择美国
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.item_relative))
        self.wait_eleVisible(loc.item_relative)
        # self.driver.find_elements(*loc.item_relative)[1].click()
        self.eles_click(loc.item_relative, 1)

    def login(self, phone, password):
        # 输入手机号
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.loginnumber_phones))
        self.wait_eleVisible(loc.loginnumber_phones)
        # self.driver.find_element(*loc.loginnumber_phones).send_keys(phone)
        self.text_input(loc.loginnumber_phones, phone)
        # 输入密码
        # self.driver.find_element(*loc.loginnumber_password).send_keys(password)
        self.text_input(loc.loginnumber_password, password)
        # 登录
        # self.driver.find_element(*loc.go_numberlogin).click()
        self.ele_click(loc.go_numberlogin)
