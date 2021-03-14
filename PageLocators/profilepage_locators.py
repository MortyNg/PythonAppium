"""
-*- coding: utf-8 -*-
File    : profilepage_locators.py
Version : 0.1
Author  : usrpi
Date    :2021/1/27
"""
from appium.webdriver.common.mobileby import MobileBy


class ProfilePageLocator:
    # 个人信息，未登录时点击打开登录页面
    my_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/my_layout')
    # 右上角设置按钮
    action_settings = (MobileBy.ID, 'com.nowcoder.app.florida:id/action_settings')
    # 昵称
    user_name_textview = (MobileBy.ID, 'com.nowcoder.app.florida:id/user_name_textview')
    # 已购按钮
    purchased_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/purchased_layout')
    # 钱包
    wallet_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/wallet_layout')
    # 身份认证
    authentication_list_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/authentication_list_layout')
    # 牛币兑换
    nowcoder_coin_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/nowcoder_coin_layout')
    # 收藏
    collect_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/collect_layout')
    # 错题
    wrong_question_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/wrong_question_layout')
    # 下载
    download_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/download_layout')
    # 最近浏览
    history_list_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/history_list_layout')
    # 动态
    my_feed_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/my_feed_layout')
    # 讨论贴
    my_discuss_post_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/my_discuss_post_layout')
    # 练习试卷
    my_test_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/my_test_layout')
    # 回答
    my_answer_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/my_answer_layout')
    # 投递管理
    deliver_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/deliver_layout')
    # 我的简历
    resume_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/resume_layout')
    # 打卡记录
    clock_list_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/clock_list_layout')
    # 页面下方设置按钮
    setting_layout = (MobileBy.ID, 'com.nowcoder.app.florida:id/setting_layout')