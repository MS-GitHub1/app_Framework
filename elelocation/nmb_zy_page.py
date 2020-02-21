#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 11:58
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
class Zy():
    #题库
    tiku = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
    # Istqb
    ISTQB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ISTQB")')
    #全程班
    qcb = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("全程班")')
    # 加群按钮
    jq = (MobileBy.XPATH, '//span[@class="course-group-title"]')
    # 等待webview元素可见
    wv = (MobileBy.CLASS_NAME, "android.webkit.WebView")