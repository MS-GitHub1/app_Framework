#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 18:31
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
class Home():
    # 我的柠檬
    nm = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')
    # 点击头像登录
    signin = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_layout')
    # 手机号
    sjh = (MobileBy.ID, 'com.lemon.lemonban:id/et_mobile')
    # 密码
    pwd = (MobileBy.ID, 'com.lemon.lemonban:id/et_password')
    # 点击登录按钮
    dl = (MobileBy.ID, 'com.lemon.lemonban:id/btn_login')
    # 题库
    tiku = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
    # 题库界面
    kj = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
    # 用户名
    yhm = (MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_avatar_title')
    # 设置按钮
    shezhi = (MobileBy.CLASS_NAME,'android.widget.ImageButton')
    # 退出登录
    tcdl = (MobileBy.ID,'com.lemon.lemonban:id/logout_button')
    # 确定按钮
    qdan = (MobileBy.ID,'com.lemon.lemonban:id/tv_sure')
    # 提示
    ts = (MobileBy.XPATH,'//*[contains(@text,"手机号码或密码")]')
    # Istqb
    ISTQB = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ISTQB")')