#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 17:54
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from Common.base import Base
from elelocation.nmb_home_page import Home as HO
from elelocation.nmb_zy_page import Zy as ZY
class NMB_login(Base):
    # 进行登录操作

    def nmb_login(self,mobile,pwd):
        self.click_ele(HO.nm,"点击我的柠檬按钮")
        self.click_ele(HO.signin,'点击头像登录按钮')
        self.send_text(HO.sjh,mobile,"输入手机号")
        self.send_text(HO.pwd,pwd,"输入密码")
        self.click_ele(HO.dl,"点击登录按钮")

    #点击题库进行页面滑动
    def click_tiku(self):
        self.click_ele(HO.tiku,"点击题库按钮")
        self.Left_and_right(HO.kj,"由上向下滑动")

    # 点击我的柠檬按钮
    def hq_xx(self):
        self.click_ele(HO.nm,"点击我的柠檬按钮")

    #获取用户名的文本值
    def success_lp(self):
       return self.get_element_text(HO.yhm,"获取")

    # 获取用户名的文本值
    def success_lo(self):
       return self.get_attr(HO.yhm,"text","wenben")

    # 点击设置按钮，进行退出
    def cl_bu(self):
        self.click_ele(HO.shezhi,"点击设置按钮")
        self.click_ele(HO.tcdl,"点击退出登录按钮")
        self.click_ele(HO.qdan,"点击确定按钮")

    # 获取提示的文本值
    def success_ts(self):
        return self.get_toast(HO.ts, "获取")

