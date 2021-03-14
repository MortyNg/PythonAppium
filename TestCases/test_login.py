"""
-*- coding: utf-8 -*-
File    : test_login.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
import unittest
from time import sleep

from appium import webdriver

from PageObjects.login_page import LoginPage
from PageObjects.welcom_page import WelcomPage
from PageObjects.profile_page import ProfilePage
from PageObjects.setting_page import SettingPage
from PageObjects.main_page import MainPage
from Datas import login_data as ld
from ddt import ddt, data
from Common.get_toast import GetToast
from Common.appstart import AppStart
from demo import driver


@ddt()
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps["automationName"] = "UIAutomator2"
        # 平台类型
        desired_caps["platformName"] = "Android"
        # 平台版本
        desired_caps["platformVersion"] = "5.1"
        # 设备名称
        desired_caps["deviceName"] = "Android Emulator"
        # app包名
        desired_caps["appPackage"] = "com.nowcoder.app.florida"
        # app入口activity
        desired_caps["appActivity"] = "com.nowcoder.app.florida.activity.home.SplashActivity"
        # app是否重置再打开
        desired_caps["noReset"] = "true"

        # 连接appium server。 前提：appium desktop要启动，有监听端口
        # 要将我们的服务器参数发送过去
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        cls.lp = LoginPage(cls.driver)
        cls.wp = WelcomPage(cls.driver)
        cls.pp = ProfilePage(cls.driver)
        cls.sp = SettingPage(cls.driver)
        cls.mp = MainPage(cls.driver)
        cls.gt = GetToast(cls.driver)

        # 欢迎页面，选择登录
        cls.wp.login_register()
        # 选择密码登录方式
        cls.lp.select_login()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) :
        # 退出登录
        cls.sp.logout()


    def test_1_login_ok(self):
        # 登录
        self.lp.login(ld.login_success["phone"], ld.login_success["password"])
        # 断言 判断设置中是否有退出按钮
        self.mp.tab_profile()
        self.pp.setting()
        sleep(2) # 等待滑屏操作
        self.assertTrue(self.sp.logout_isExsit())

    @data(*ld.login_error)
    def test_0_login_error(self,data):
        # 输入账号和密码登录
        self.lp.login(data['phone'], data['password'])
        # 断言
        self.assertEqual(self.gt.get_toast(data['check']), data['check'])


