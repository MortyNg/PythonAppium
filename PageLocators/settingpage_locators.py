"""
-*- coding: utf-8 -*-
File    : settingpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium.webdriver.common.mobileby import MobileBy


class SettingPageLocator:
    # 退出登录
    logout_text_view = (MobileBy.ID, 'com.nowcoder.app.florida:id/logout_text_view')