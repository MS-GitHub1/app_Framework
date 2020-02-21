"""
1、usb连接了一个设备(android5.1)到电脑端，开启了USB调试模式
2、appium server  --(android/IOS)
3、python代码

任务：通过写一段python代码，在android设备上，打开 柠檬班app.

1、你告诉appium server，你要在XX设备上，打开XXapp
2、appium收到你的命令之后，检测一下是否有XX设备，检测一下设备上是否有XXapp
3、2)确认成功，就执行命令。

获取应用包名和入口activity：aapt命令
aapt目录：
安卓sdk的build-tools目录下
示例：adt-bundle-windows-x86_64-20140702\sdk\build-tools\android-4.4W
命令语法：
aapt dump badging apk应用名
示例：aapt dump badging D:\BaiduNetdiskDownload\Future-release-2018.apk
"""
import time
from Common.base import Base
from elelocation.nmb_home_page import Home as ec
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
ys = (MobileBy.ID,'com.lemon.lemonban:id/navigation_my')
wait.until(EC.visibility_of_element_located(ys))
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.lemon.lemonban:id/navigation_my")').click()

me = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("我的柠檬")')
driver.find_element(*me).click()
time.sleep(1)
driver.start_activity("com.xxzb.fenwoo","com.xxzb.fenwoo.activity.addition.WelcomeActivity")
time.sleep(1)

# signin = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
# wait.until(EC.visibility_of_element_located(signin))
# driver.find_element(*signin).click()
#
# dl = (MobileBy.ID, 'com.lemon.lemonban:id/btn_login')
# wait.until(EC.visibility_of_element_located(dl))
# driver.find_element(*dl).click()
#
# loc = (MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
# wait.until(EC.presence_of_element_located(loc))
# asa = driver.find_element(*loc).text
# print(asa)


