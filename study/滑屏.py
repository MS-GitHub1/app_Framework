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
    "appPackage": "com.lemon.lemonban", # 包名
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"  # 入口页面: activity
}

# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,20)

# 等待题 库
loc = (MobileBy.ID,"com.lemon.lemonban:id/navigation_tiku")
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待题 库类型都可见
loc = (MobileBy.ID,"com.lemon.lemonban:id/fragment_category_type")
wait.until(EC.visibility_of_all_elements_located(loc))
time.sleep(1)
"""
swipe: 滑屏操作。

"""
# 整个设备的大小
# 整个高和宽
device_size = driver.get_window_size()
# 从下向上滑动
driver.swipe(device_size["width"]*0.5,device_size["height"]*0.85,device_size["width"]*0.5,device_size["height"]*0.15,200)

# 从上向下滑动
driver.swipe(device_size["width"]*0.5,device_size["height"]*0.15,device_size["width"]*0.5,device_size["height"]*0.85,200)

# 从左到右滑动
driver.swipe(device_size["width"]*0.15,device_size["height"]*0.5,device_size["width"]*0.85,device_size["height"]*0.5,200)

# 从右到左滑动
driver.swipe(device_size["width"]*0.85,device_size["height"]*0.5,device_size["width"]*0.15,device_size["height"]*0.5,200)

driver.tap()