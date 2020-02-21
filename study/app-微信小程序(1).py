#!/usr/bin/python3
"""
@File    : app_keycode.py
@Time    : 2019/11/01 15:42
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

"""
当前所有的上下文为： ['NATIVE_APP', 'WEBVIEW_com.tencent.mm', 'WEBVIEW_com.tencent.mm:toolsmp', 'WEBVIEW_com.tencent.mm:tools', 'WEBVIEW_com.tencent.mm:appbrand0']
当前所有的窗口为： ['CDwindow-20DA4A7CD0DAC2B9FC1DF674223F2E29', 'CDwindow-1591A58E3FDC4CBA23D87686209C4092', 'CDwindow-771B330B93A106E2989075DF9A281C2F']
切换到窗口： CDwindow-20DA4A7CD0DAC2B9FC1DF674223F2E29
切换到窗口： CDwindow-1591A58E3FDC4CBA23D87686209C4092
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy as MB

#引入appium包
from appium import webdriver
import time
import os
"""
1\识别
2、开启调试：
针对微信版本在7.0+，微信有对H5开关做了调整，需要在聊天窗口输入如下：
http://debugmm.qq.com/?forcex5=true
http://debugx5.qq.com

3、appium代码当中：
   #支持X5内核应用自动化配置  desired_caps["recreateChromeDriverSessions"] = True
   # desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand0"}  # 小程序在哪个进程 
   
按微信小程序调试入口，进入到小程序页面。 发现 - 搜一搜 - 搜索 柠檬班软件测试

4、进入小程序之后，获取当前所有的上下文，切换进最后一个webview
   chromedriver版本要与腾讯x5版本匹配，而不是原生的webview

5、获取小程序当中所有的窗口。
   遍历所有窗口，并切入窗口的html中，查找有代表性的元素。
   driver.find_element
   driver.page_source.find("") != -1:
      break
"""

#启动appium时，需要指定chromedriver.exe的目录。使用appium默认目录下的会报错。
#在切换到小程序webview时，会去匹配chrome内核的39的驱动。在切换完成之后，在打印所有的窗口时，会使用x5内核的版本。
#所以指定一个非默认目录下面的chromedriver.exe(X5内核对应的版本)，此问题就不会出现 。
#在appium server上设置chromedriver的路径：D:\ChromeDrivers\chromedriver.exe
desired_caps = {}
#支持X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"] = True
#android 4.4以下的版本通过Selendroid来切换到webview
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "OPPO R7sm"
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps["noReset"] = True

# ChromeOptions使用来定制启动选项，因为在appium中切换context识别webview的时候,
# 把com.tencent.mm:toolsmp的webview识别成com.tencent.mm的webview.
# 所以为了避免这个问题，加上androidProcess: com.tencent.mm:toolsm
# options = wb.ChromeOptions()
# options.add_experimental_option("androidProcess","com.tencent.mm:toolsmp")
desired_caps["chromeOptions"] = {"androidProcess":"com.tencent.mm:appbrand0"}
# desired_caps["browserName"] = ""

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# driver.implicitly_wait(30)

#
# time.sleep(5)
# #点击发现
# driver.find_element_by_xpath('//*[@text=\"发现\"]').click()
#点击发现里面搜一搜
# driver.find_element_by_xpath('//*[@text=\"搜一搜\"]').click()


# #等待搜索框出现
# loc = (MB.XPATH,'//*[contains(@text,"搜索")]')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
# #点击搜索框
# driver.find_element(*loc).click()
# driver.find_element(*loc).send_keys("柠檬班软件测试")
# time.sleep(5)
# # #点击历史记录中的柠檬班软件测试（采用adb命令坐标点击的方式)
# # print(driver.contexts)
# os.system("adb shell input tap 330 194")
# # #点击柠檬班软件测试小程序
# time.sleep(5)
# os.system("adb shell input tap 350 455")
# # #等待小程序加载完成
# time.sleep(5)
# #获取所有的上下文
# cons = driver.contexts
# print("当前所有的上下文为：",cons)
#
# #切换到小程序webview
# driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
# time.sleep(5)
#
# print("=================进入web自动化环节===============================")
# #打印当前所有的窗口
# hs = driver.window_handles
# print("当前所有的窗口为：",hs)
# # # #print("当前所在的窗口为：",driver.current_window_handle)
# # # #需要找到哪一个窗口有柠檬班信息的窗口，然后再在其下找元素操作。
# # # #遍历所有的handles，找到当前页面所在的handle：如果pageSource有包含你想要的元素，就是所要找的handle
# # # #小程序的页面来回切换也需要：遍历所有的handles，切换到元素所在的handle
for handle in hs:
    driver.switch_to.window(handle)
    print("切换到窗口：",handle)
    time.sleep(3)
    #print(driver.page_source)
    if driver.page_source.find("柠檬班") != -1:
        break
# # #
#点击老师
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MB.XPATH,"//*[@id=\"js-tab-bar\"]/li[3]"))).click()

WebDriverWait(driver,20).until(EC.presence_of_element_located((MB.XPATH,"//em[text()='歪歪']")))
time.sleep(0.5)
# #找到歪歪老师
ele = driver.find_element_by_xpath("//em[text()='歪歪']")
# # #拖动到可见区域
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.click()
# #
#
#



