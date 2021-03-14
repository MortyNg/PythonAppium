"""
-*- coding: utf-8 -*-
File    : loginpage_locators.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocators:

    # 验证码登录，手机号输入框
    loginnumber_phones = (MobileBy.ID, 'com.nowcoder.app.florida:id/loginnumber_phones')
    # 验证码登录，验证码输入框
    code_textview = (MobileBy.ID, 'com.nowcoder.app.florida:id/code_textview')
    # 验证码登录，获取验证码
    re_resend_code = (MobileBy.ID, 'com.nowcoder.app.florida:id/re_resend_code')
    # 验证码登录，区号
    country_textview = (MobileBy.ID, 'com.nowcoder.app.florida:id/country_textview')
    # 选择区号
    item_relative = (MobileBy.ID, 'com.nowcoder.app.florida:id/item_relative')
    # 验证码登录，注册登录按钮
    go_numberlogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/go_numberlogin')
    # 微信
    goto_wxlogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_wxlogin')
    # 微博
    goto_sinalogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_sinalogin')
    # QQ
    goto_qqlogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_qqlogin')
    # 密码登录、验证码登录
    btn_switch_veritype = (MobileBy.ID, 'com.nowcoder.app.florida:id/btn_switch_veritype')
    # 密码登录，密码输入框
    loginnumber_password = (MobileBy.ID, 'com.nowcoder.app.florida:id/loginnumber_password')
    # 密码登录，登录按钮
    go_numberlogin = (MobileBy.ID, 'com.nowcoder.app.florida:id/go_numberlogin')
    # 密码登录，海外手机登录
    goto_oversea_page = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_oversea_page')
    # 密码登录，忘记密码
    goto_lostpsw_page = (MobileBy.ID, 'com.nowcoder.app.florida:id/goto_lostpsw_page')

    # 账号不能为空
    phone_null = (MobileBy.XPATH, '//*[contains(@text,"账号不能为空")]')
    # 密码不能为空
    password_null = (MobileBy.XPATH, '//*[contains(@text,"密码不能为空")]')
    # 账户或密码错误
    phone_password_error = (MobileBy.XPATH, '//*[contains(@text,"账户或密码错误")]')
    # 账户格式错误，请输入正确的邮箱或手机号码
    phone_format_error = (MobileBy.XPATH, '//*[contains(@text,"账户格式错误，请输入正确的邮箱或手机号码")]')
