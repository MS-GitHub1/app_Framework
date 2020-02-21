#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 16:29
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 20:36
# @Author  : Lynn
# @Site    :
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
desired_caps = {
    "automationName":"appium" ,
    # 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"5.1.1",  # 系统版本号
    "deviceName":"vivo",  # 设备名称  uuid
    "noReset":True,  # 应用不重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.lemon.lemonban", # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities= desired_caps)
dirver_size = driver.get_window_size()
# 点击题库
tiku = (MobileBy.ID,'com.lemon.lemonban:id/navigation_tiku')
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(tiku))
driver.find_element(*tiku).click()

# 手机滑动
# 由下向上
# driver.swipe(dirver_size["width"]*0.25,dirver_size["height"]*0.85,dirver_size["width"]*0.25,dirver_size["height"]*0.15,200)
# 由上向下
# driver.swipe(dirver_size["width"]*0.25,dirver_size["height"]*0.15,dirver_size["width"]*0.25,dirver_size["height"]*0.7,200)
# 由左向右
# driver.swipe(dirver_size["width"]*0.10,dirver_size["height"]*0.15,dirver_size["width"]*0.8,dirver_size["height"]*0.15,200)
#由右向走
# driver.swipe(dirver_size["width"]*0.90,dirver_size["height"]*0.15,dirver_size["width"]*0.8,dirver_size["height"]*0.1,200)

old = None
new = driver.page_source
while old != new:
    try:
        loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ISTQB")')
        kj = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
        wait.until(EC.visibility_of_all_elements_located(kj))
        time.sleep(1)
        ele = driver.find_element(*loc).click()
    except:
        driver.swipe(dirver_size["width"] * 0.25, dirver_size["height"] * 0.85, dirver_size["width"] * 0.25,
                     dirver_size["height"] * 0.25, 200)
        old = new
        new = driver.page_source
    else:
        print("zzzzz")
        break

