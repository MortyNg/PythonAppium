"""
-*- coding: utf-8 -*-
File    : appstart.py
Version : 0.1
Author  : usrpi
Date    :2021/2/2
"""
from appium.webdriver import webdriver


class AppStart:

    def start(self):
        desired_caps = {
            "automationName" : "UIAutomator2",
            "platformName" : "Android",
            "platformVersion" : "5.1",
            "deviceName" : "Android Emulator",
            "appPackage" : "com.nowcoder.app.florida",
            "appActivity" : "com.nowcoder.app.florida.activity.home.SplashActivity",
            "noReset" :  "true"
        }
        # desired_caps["automationName"] = "UIAutomator2"
        # # 平台类型
        # desired_caps["platformName"] = "Android"
        # # 平台版本
        # desired_caps["platformVersion"] = "5.1"
        # # 设备名称
        # desired_caps["deviceName"] = "Android Emulator"
        # # app包名
        # desired_caps["appPackage"] = "com.nowcoder.app.florida"
        # # app入口activity
        # desired_caps["appActivity"] = "com.nowcoder.app.florida.activity.home.SplashActivity"
        # # app是否重置再打开
        # desired_caps["noReset"] = "true"

        # 连接appium server。 前提：appium desktop要启动，有监听端口
        # 要将我们的服务器参数发送过去
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

