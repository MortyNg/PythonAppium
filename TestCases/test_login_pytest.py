"""
-*- coding: utf-8 -*-
File    : test_login.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""

import pytest
from time import sleep

from appium import webdriver

from PageObjects.login_page import LoginPage
from PageObjects.welcom_page import WelcomPage
from PageObjects.profile_page import ProfilePage
from PageObjects.setting_page import SettingPage
from PageObjects.main_page import MainPage
from TestDatas import login_data as ld
from Common.basepage import BasePage

# 在每次用例开始前和结束后都去执行一次
# 还有更高级的setupClass 和 teardownClass，需要配合@classmethod装饰器一起使用
# 在做selenium自动化的时候，它的效率尤为突出，可以只启动一次浏览器执行多个用例

# 用例执行顺序使用 @pytest.mark.run(order=x)，需先pip install pytest-ordering
# 标记于被测试函数，@pytest.mark.run(order=x)
# 根据 order 传入的参数来解决运行问题
# order 值全为正数或全为负数时，值越小，优先级越高
# 正数和负数同时存在时，正数优先级高
'''
模块级（setup_module/teardown_module)开始于模块始末，全局的
函数级（setup_function/teardown_function)只对函数用例生效（不在类中）
类级（setup_class/teardown_class)只在类中前后运行一次（在类中）
方法级（setup_method/teardown_method)开始于方法始末（在类中）
类里面的（setup/teardown)运行在调用方法的前后
'''
#
class TestLogin():

    @classmethod
    def setup_class(cls):

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
        cls.bp = BasePage(cls.driver)


        # 欢迎页面，选择登录
        cls.wp.login_register()
        # 选择密码登录方式
        cls.lp.select_login()

    def setup(self) -> None:
        pass

    def teardown(self) -> None:
        pass

    @classmethod
    def teardown_class(cls) :
        # 退出登录
        cls.sp.logout()
        # pass

    # @pytest.mark.skip
    @pytest.mark.run(order=2)
    def test_login_ok(self):
        # 登录
        self.lp.login(ld.login_success["phone"], ld.login_success["password"])
        # 断言 判断设置中是否有退出按钮
        self.mp.tab_profile()
        self.pp.setting()
        sleep(2) # 等待滑屏操作
        # self.assertTrue(self.sp.logout_isExsit()) # unittest 的断言方式
        assert self.sp.logout_isExsit() == True # pytest 使用python自带的断言

    @pytest.mark.run(order=1) # 设置用例执行顺序
    @pytest.mark.parametrize('dic',ld.login_error) # 参数化
    def test_login_error(self, dic):
        # 输入账号和密码登录
        self.lp.login(dic['phone'], dic['password'])
        # 断言
        # self.assertEqual(self.gt.get_toast(dic['check']), dic['check'])
        assert self.bp.get_toast(dic['check']) == dic['check'] # pytest 使用python自带的断言


if __name__ == '__main__':
    pytest.main(['-vs','test_login_pytest.py'])