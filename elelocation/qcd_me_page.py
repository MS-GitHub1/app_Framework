#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 21:09
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from appium.webdriver.common.mobileby import MobileBy
class Me_page():
    # 安全中心
    anquan = (MobileBy.ID, 'com.xxzb.fenwoo:id/textView11')
    # 手势密码
    ssmm = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_gesture_password')
    # 设置手势密码
    sz = (MobileBy.ID, 'com.xxzb.fenwoo:id/layout_update_gesture')
    # 创建手势密码
    cjsj = (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_gesturepwd_guide')
    #确定按钮
    ssqd = (MobileBy.ID, 'com.xxzb.fenwoo:id/right_btn')
    # 继续按钮
    jx = (MobileBy.ID, 'com.xxzb.fenwoo:id/right_btn')
    # 画画
    tuan = (MobileBy.ID, 'com.xxzb.fenwoo:id/gesturepwd_create_lockview')