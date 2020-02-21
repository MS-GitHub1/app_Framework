"""
android.webkit.WebView   里面放的是一个html页面。

1、识别

2、打开app的调试模式：开启应用的webview debug模式。

3、从原生控件，切换到html当中。
   上下文(context) driver.switch_to.context()
   默认的context: NATIVE_APP
   html：context: WebView_XXXXXX

   1) 要得到所有的上下文  driver.contexts    # 列表
   前提：开启应用的webview debug模式。

   2）切换到webview当中。
   driver.switch_to.context()

4、得到html页面源码，定位元素。
   1) driver.page_source
   2) uc-devtools (使用前提：adb devices;2) webview的调试模式；3）设备要是在webview的页面)
   3) chrome浏览器当中，chrome://inspect (需要科学上网工具辅助)

5、web自动化当中，驱动程序 - chromedriver（当前设备的webview版本匹配）
"""

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
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",  # 入口页面: activity
    "chromedriverExecutable":"E:\\Program Files\\chromedriver\\52\\chromedriver.exe"

}

# ****************************   APP自动化   *****************************
# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
wait = WebDriverWait(driver,20)

# 点击全程班
loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("全程班")')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待webview元素可见
loc = (MobileBy.CLASS_NAME,"android.webkit.WebView")
time.sleep(2)

# 获取当前所有的contexts
cons = driver.contexts
print(cons)
# 获取当前的context
print(driver.current_context)

# 切换
driver.switch_to.context(cons[1])
# 进入了html页面。

# ****************************   WEB自动化   *****************************
loc12 = (MobileBy.XPATH,'//span[@class="course-group-title"]')
wait.until(EC.visibility_of_element_located(loc12))
driver.find_element(*loc12).click()