"""
-*- coding: utf-8 -*-
File    : mainpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators:

    tab_study = (MobileBy.ID, 'com.nowcoder.app.florida:id/tab_study')
    comtab_communitymunity = (MobileBy.ID, 'com.nowcoder.app.florida:id/tab_community')
    tab_job = (MobileBy.ID, 'com.nowcoder.app.florida:id/tab_job')
    tab_message = (MobileBy.ID, 'com.nowcoder.app.florida:id/tab_message')
    tab_profile = (MobileBy.ID, 'com.nowcoder.app.florida:id/tab_profile')