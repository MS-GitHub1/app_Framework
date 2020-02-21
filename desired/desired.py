#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 16:17
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
desired_caps = {
    # "automationName":"appium" # 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"5.1.1",  # 系统版本号
    "deviceName":"vivo",  # 设备名称
    "noReset":True,  # 应用不重置
    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.xxzb.fenwoo", # 包名
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity"  # 入口页面: activity
}

desired_nmb = {
    "automationName":"uiautomator2",# 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"5.1.1",  # 系统版本号
    "deviceName":"vivo",  # 设备名称
    "noReset":True,  # 应用不重置
    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban", # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",  # 入口页面: activity
    "chromedriverExecutable":"E:\\Program Files\\chromedriver\\52\\chromedriver.exe"
}


url = {"url" : "http://127.0.0.1:4723/wd/hub"}