"""
放大缩小
"""
from appium.webdriver.common.multi_action import MultiAction

from appium.webdriver.common.touch_action import TouchAction

from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

desired_caps = {
    # "automationName":"appium" # 自动化引擎,不设置的话,默认为appium.
    "platformName":"Android",  # 操作系统
    "platformVersion":"5.1",  # 系统版本号
    "deviceName":"huawei",  # 设备名称
    "noReset":True,  # 应用不重置

    # app: 独一无二的包名.  入口页面: activity
    "appPackage": "com.baidu.BaiduMap", # 包名
    "appActivity": "com.baidu.baidumaps.WelcomeScreen"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,20)

# 整个高和宽
device_size = driver.get_window_size()

time.sleep(20)

# 从中间划到左下
t1 = TouchAction(driver).press(x=device_size["width"]*0.4,y=device_size["height"]*0.5).wait(200).\
    move_to(x=device_size["width"]*0.1,y=device_size["height"]*0.95).release()

# 从中间划到右上
t2 = TouchAction(driver).press(x=device_size["width"]*0.4,y=device_size["height"]*0.5).wait(200).\
    move_to(x=device_size["width"]*0.9,y=device_size["height"]*0.1).release()

# 从中间划到右上
t3 = TouchAction(driver).press(x=device_size["width"]*0.4,y=device_size["height"]*0.5).wait(200).\
    move_to(x=device_size["width"]*0.1,y=device_size["height"]*0.1).release()

mm = MultiAction(driver)
mm.add(t1,t2,t3)
mm.perform()