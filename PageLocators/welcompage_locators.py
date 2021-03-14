"""
-*- coding: utf-8 -*-
File    : welcompage_locators.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium.webdriver.common.mobileby import MobileBy


class WelcomPageLocator:
    # 登录注册
    gotoLoginView = (MobileBy.ID, 'com.nowcoder.app.florida:id/gotoLoginView')
    # 随便看看
    gotoMainView = (MobileBy.ID, 'com.nowcoder.app.florida:id/gotoMainView')