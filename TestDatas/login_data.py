"""
-*- coding: utf-8 -*-
File    : login_data.py
Version : 0.1
Author  : usrpi
Date    :2021/1/28
"""

login_success = {"phone":"5678250990", "password":"Aa112211"}

login_error =[
{'phone':'', 'password':'', 'check':'账号不能为空'},
{'phone':'   ', 'password':'123456', 'check':'账号不能为空'},
{'phone':'5678250990', 'password':'', 'check':'密码不能为空'},
{'phone':'111', 'password':'111', 'check':'账户或密码不正确'},
{'phone':'111qw', 'password':'111', 'check':'账户格式错误，请输入正确的邮箱或手机号码'},
              ]