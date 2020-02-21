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
from appium.webdriver.common.mobileby import MobileBy
from Common.base import Base
name ={"sjh":"15831268320","pws":268320}

# 整个高和宽
# device_size = base.get_window_size()

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

class Login_ome(Base):
    def login(self):
        self.click_ele(me,"点击")



