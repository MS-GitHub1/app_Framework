#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 19:02
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.touch_action import TouchAction
'''
press  按住
release  释放
long-press 长按
wait  等待
move_to  移动
'''
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
name ={"sjh":"15831268320","pws":268320}
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
napw={"name":"18684720553","pwd":"python"}
# 与appium server建立连接
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# 整个高和宽
device_size = driver.get_window_size()

me=(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("我")')
sjh = (MobileBy.ID,'com.xxzb.fenwoo:id/et_phone')
xyb = (MobileBy.ID,'com.xxzb.fenwoo:id/btn_next_step')
pwd = (MobileBy.ID,'com.xxzb.fenwoo:id/et_pwd')
qd = (MobileBy.ID,'com.xxzb.fenwoo:id/btn_next_step')
anquan = (MobileBy.ID,'com.xxzb.fenwoo:id/textView11')
ssmm = (MobileBy.ID,'com.xxzb.fenwoo:id/layout_gesture_password')
sz = (MobileBy.ID,'com.xxzb.fenwoo:id/layout_update_gesture')
cjsj = (MobileBy.ID,'com.xxzb.fenwoo:id/btn_gesturepwd_guide')
ssqd = (MobileBy.ID,'com.xxzb.fenwoo:id/right_btn')
jx = (MobileBy.ID,'com.xxzb.fenwoo:id/right_btn')
tuan = (MobileBy.ID,'com.xxzb.fenwoo:id/gesturepwd_create_lockview')

wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(me))
driver.find_element(*me).click()
wait.until(EC.visibility_of_element_located(sjh))
driver.find_element(*sjh).send_keys(napw["name"])
driver.find_element(*xyb).click()
wait.until(EC.visibility_of_element_located(pwd))
driver.find_element(*pwd).send_keys(napw["pwd"])
driver.find_element(*qd).click()
wait.until(EC.visibility_of_element_located(anquan))
driver.find_element(*anquan).click()
wait.until(EC.visibility_of_element_located(ssmm))
driver.find_element(*ssmm).click()
wait.until(EC.visibility_of_element_located(sz))
driver.find_element(*sz).click()
wait.until(EC.visibility_of_element_located(cjsj))
driver.find_element(*cjsj).click()
wait.until(EC.visibility_of_element_located(ssqd))
driver.find_element(*ssqd).click()
wait.until(EC.visibility_of_element_located(jx))
# 使用TouchActions
ta = TouchAction(driver)
#获取起点
ele = driver.find_element(*tuan)
#获取起点
qidian = ele.location
size = ele.size

step = size["width"]/6

p1 = (qidian["x"]+step,qidian["y"]+step)
p2 = (p1[0] + 2*step,p1[1])
p3 = (p2[0] + 2*step,p2[1])
p4 = (p3[0],p3[1] + 2*step)
p5 = (p4[0],p4[1] + 2*step)
p6 = (p5[0] - 2*step,p5[1])

ta.press(x=p1[0],y=p1[1]).wait(200).\
    move_to(x=p2[0],y=p2[1]).wait(200).\
    move_to(x=p3[0],y=p3[1]).wait(200).\
    move_to(x=p4[0],y=p4[1]).wait(200).\
    move_to(x=p5[0],y=p5[1]).wait(200).\
    move_to(x=p6[0],y=p6[1]).wait(200).\
    release().perform()

