#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 18:06
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.multi_action import MultiAction

from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import os
import time

desired_caps = {
    "recreateChromeDriverSessions":  True,
    "automationName":"appium", # 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"8.0.0",  # 系统版本号
    "deviceName":"MIX 2S",  # 设备名称
    "noReset":True,  # 应用不重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.tencent.mm", # 包名
    "appActivity": "com.tencent.mm.ui.LauncherUI" , # 入口页面: activity
    # "chromeOptions": {"androidProcess":"com.tencent.mm:appbrand0"}
    # 进程
    "chromeOptions" :{"androidProcess":"com.tencent.mm:appbrand0"},
    "chromedriverExecutable":"E:\\Program Files\\chromedriver\\66\\chromedriver.exe"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
faxian = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("发现")')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(faxian))
# #点击发现
driver.find_element(*faxian).click()
driver.find_element_by_xpath('//*[@text=\"发现\"]').click()
# 点击发现里面搜一搜
driver.find_element_by_xpath('//*[@text=\"搜一搜\"]').click()
#等待搜索框出现
loc = (MobileBy.XPATH,'//*[contains(@text,"搜索")]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
#点击搜索框
driver.find_element(*loc).click()
lo = (MobileBy.ID,'com.tencent.mm:id/m7')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(lo))
driver.find_element(*lo).send_keys("柠檬班软件测试")
time.sleep(1)
os.system("adb shell input tap 148 287")
time.sleep(5)
os.system("adb shell input tap 160 985")
time.sleep(6)
cons = driver.contexts
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
op = driver.window_handles
for i in op:
    driver.switch_to.window(i)
    print("进入到窗口{}".format(i))
    time.sleep(2)
    # if driver.page_source.find("柠檬班") != -1:
    try:
        le = driver.find_element_by_xpath('//h1[@class="header__name"]').text
        le = "柠檬班"
    except:
        print("没有找到")
    else:
        break
time.sleep(2)

ys = (MobileBy.XPATH, '//h1[@class="header__name"]')
ys1 = driver.find_element(*ys).text
print(ys1)
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.XPATH,"//*[@id=\"js-tab-bar\"]/li[2]"))).click()
#
# WebDriverWait(driver,20).until(EC.presence_of_element_located((MobileBy.XPATH,'//ul[@class="second-class__list"]//li[1]')))
#
# time.sleep(0.5)
# # #找到歪歪老师
# ele = driver.find_element_by_xpath('//ul[@class="second-class__list"]//li[1]')
#
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# time.sleep(2)

# driver.find_element_by_xpath('//ul[@class="second-class__list"]//li[1]').click()