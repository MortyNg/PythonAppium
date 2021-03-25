"""
-*- coding: utf-8 -*-
File    : dir_config.py
Version : 0.1
Author  : usrpi
Date    :2021/3/16
"""
import os
# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

tesdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

htmlreport_dir = os.path.join(base_dir, "Outputs/Reports")

logs_dir = os.path.join(base_dir, "Outputs/Logs")

screenshot_dir = os.path.join(base_dir, "Outputs/Screenshots")