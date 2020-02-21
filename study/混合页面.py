#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 19:54
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
name ={"sjh":"15831268320","pws":268320}
desired_caps = {
    "automationName":"uiautomator2", # 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"5.1.1",  # 系统版本号
    "deviceName":"vivo",  # 设备名称
    "noReset":True,  # 应用不重置
    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban", # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,20)
driver.get_window_size()

loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("全程班")')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
con = driver.contexts

driver.switch_to.context('WEBVIEW_com.lemon.lemonban')