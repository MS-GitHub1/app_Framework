#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 21:02
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
class Home():
    # 首页中的“我”
    me = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我")')
    # 手机号码
    sjh = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_phone')
    # 下一步
    xyb = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')
    # 密码
    pwd = (MobileBy.ID, 'com.xxzb.fenwoo:id/et_pwd')
    # 确定按钮
    qd = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_next_step')